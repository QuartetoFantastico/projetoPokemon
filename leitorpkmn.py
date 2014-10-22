from sys import stdin
import ataque
import re

class Leitor:

	def __init__(self):
		self.line = stdin.readline()
		self.listaAtributosPokemon = []
		self.listaAtributosAtk = []

	def leitorDePokemons(self):

		while (self.line is not None and len(self.listaAtributosPokemon) < 10):
			atributos = self.line.split()
			self.listaAtributosPokemon.extend(atributos)
			self.line = stdin.readline()
		
		length = len(self.listaAtributosPokemon)
		if (length < 10):
			print("Pokemon inválido!")
			return []

		if (length >= 10):
			self.listaAtributosAtk = self.listaAtributosPokemon[10:length]
			self.listaAtributosPokemon = self.listaAtributosPokemon[0:10]

		nome = self.listaAtributosPokemon.pop(0)
		try:
			self.listaAtributosPokemon = [int(i) for i in self.listaAtributosPokemon]
		except ValueError:
			print("ERRO: ALGUM ATRIBUTO DO POKEMON FALTANDO")
		self.listaAtributosPokemon.insert(0, nome)


		listaAtks = []
		for i in range (0, self.listaAtributosPokemon[9]):
			atk = self.leitorDeAtk()
			if (atk is None):
				self.listaAtributosPokemon.extend(listaAtks)
				return self.listaAtributosPokemon
			listaAtks.append(atk)
		self.listaAtributosPokemon.extend(listaAtks)

		return self.listaAtributosPokemon


	def leitorDeAtk(self):

		atk = ataque.Ataque()
		cont = len(self.listaAtributosAtk)
		while (self.line is not None and len(self.listaAtributosAtk) < 5):
			atributos = self.line.split()
			self.listaAtributosAtk.extend(atributos)
			self.line = stdin.readline()

		if (len(self.listaAtributosAtk) < 5): return None

		p = re.compile('[a-zA-Z]+')
		if (p.match(self.listaAtributosAtk[1])):
			atk.nome = self.listaAtributosAtk.pop(0) + ' ' + self.listaAtributosAtk.pop(0)
			if (self.line is not None):
				atributos = self.line.split()
				self.listaAtributosAtk.extend(atributos)
				self.line = stdin.readline()
			else: print("Ataque inválido!")
		else: atk.nome = self.listaAtributosAtk.pop(0)


		atributos = self.listaAtributosAtk[0:4]
		self.listaAtributosAtk = self.listaAtributosAtk[4:len(self.listaAtributosAtk)]

		if (len(atributos) < 4):
			print("Ataque inválido!")
			return None

		try:
			atributos = [int(i) for i in atributos]
		except ValueError:
			print("ERRO: ALGUM ATRIBUTO DO ATAQUE FALTANDO")


		atk.typ = atributos.pop(0)
		atk.acu = atributos.pop(0)
		atk.pwr = atributos.pop(0)
		atk.pp = atributos.pop(0)
		atk.ppAtual = atk.pp

		return atk
