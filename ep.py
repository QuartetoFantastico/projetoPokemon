from sys import stdin
import re


class Batalha:

	def IniciaTurno(self):
		if (pkmn.spd > pkmn2.spd):
			return pkmn
		elif (pkmn2.spd > pkmn.spd):
			return pkmn2
		else:
		    return random.randint(1, 3)	


	def EscolheAtaque(self):
		number = int(input("Escolha o número do ataque"))

	def TypeChart(self, name):
		arquivo = open(name, 'r')
		tab = []
		i = 0
		line = arquivo.readline()
		while(line):
			tab.append(line)
			tab[i] = tab[i].split()
			tab[i] = [float(j) for j in tab[i]]
			i+= 1
			line = arquivo.readline()


		for i in range(0, len(tab) - 1):
			print(tab[i])	
		return tab


	def StabBonus():
		if (atk.typ == pkmn.typ1 or atk.typ == pkmn.typ2): return 1.5
		return 1

	def CriticalHit():
		critical = (pkmn.spd/512);
		temp = random.uniform(0, 1)
		if (temp <= critical):
			return (2 * pkmn.lvl + 5)/(pkmn.lvl+5)
		return 1

	def CalculaDano(self, atk):

		critical = CriticalHit();
		tab = TypeChart();
		STAB = StabBonus()
		Type = tab[atk.typ][pkmn2.typ1] * [atk.typ][pkmn2.typ2] 
		Modifier = STAB * Type * Critical * random.uniform(0.85, 1)
		Damage = ((2 * pkmn.lvl + 10)/250 * pkmn.atk/pkmn2.defe * atk.pwr + 2) * Modifier;
		
class Pokemon:

	def __init__(self):
		leitor = Leitor()
		lista = leitor.leitorDePokemons()
		print(lista)
		if (len(lista) >= 10):
			self.nome = lista.pop(0)
			self.lvl = lista.pop(0)
			self.hp = lista.pop(0)
			self.atk = lista.pop(0)
			self.defe = lista.pop(0)
			self.spd = lista.pop(0)
			self.spc = lista.pop(0)
			self.typ1 =lista.pop(0)
			self.typ2 = lista.pop(0)
			lista.pop(0)
			while (len(lista) < 4):
				lista.append(None)
			self.atks = lista

	def isAlive(self):
		return (self.hpAtual > 0)

	def show(self):
		print()
		print('Nome: {}'.format(self.nome))
		print('Level: {}'.format(self.lvl))
		print('HP: {}'.format(self.hp))
		print('Ataque: {}'.format(self.atk))
		print('Defesa: {}'.format(self.defe))
		print('Speed: {}'.format(self.spd))
		print('Tipos: {} e {}'.format(self.typ1, self.typ2))
		print()
		print('Moves:')
		for i in range(0,4):
			if (self.atks[i] is not None):
				self.atks[i].show()

class Ataque:

	def __init__(self):
		self.nome = ''
		self.typ = -1
		self.acu = -1
		self.pwr = -1
		self.pp = -1
		self.ppAtual = -1 

	def show(self):
		print('\tNome: {}'.format(self.nome))
		print('\tTipo: {}'.format(self.typ))
		print('\tAccuracy: {}'.format(self.acu))
		print('\tPower: {}'.format(self.pwr))
		print('\tPP: {}/{}'.format(self.ppAtual,self.pp))
		print()

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
		print(self.listaAtributosPokemon)
		self.listaAtributosPokemon = [int(i) for i in self.listaAtributosPokemon]
		self.listaAtributosPokemon.insert(0, nome)
		print(self.listaAtributosPokemon)

		listaAtks = []
		for i in range (0, self.listaAtributosPokemon[9]):
			listaAtks.append(self.leitorDeAtk())
		self.listaAtributosPokemon.extend(listaAtks)

		return self.listaAtributosPokemon

	def leitorDeAtk(self):

		atk = Ataque()
		cont = len(self.listaAtributosAtk)
		while (self.line is not None and len(self.listaAtributosAtk) < 5):
			atributos = self.line.split()
			self.listaAtributosAtk.extend(atributos)
			self.line = stdin.readline()

		p = re.compile('[a-zA-Z]+')
		if (p.match(self.listaAtributosAtk[1])):
			atk.nome = self.listaAtributosAtk.pop(0) + ' ' + self.listaAtributosAtk.pop(0)
			if (self.line is not None):
				atributos = self.line.split()
				self.listaAtributosAtk.extend(atributos)
				self.line = stdin.readline()
			else: print("Ataque inválido!")
		else: atk.nome = self.listaAtributosAtk.pop(0)

		self.listaAtributosAtk = [int(i) for i in self.listaAtributosAtk]
		atk.typ = self.listaAtributosAtk.pop(0)
		atk.acu = self.listaAtributosAtk.pop(0)
		atk.pwr = self.listaAtributosAtk.pop(0)
		atk.pp = self.listaAtributosAtk.pop(0)
		atk.ppAtual = atk.pp

		return atk



# leitor = Leitor()
# pkmn = leitor.leitorDePokemon()
# pkmn2 = leitor.leitorDePokemon()


# battle = Batalha()
# battle.TypeChart('tabela.txt')    

pkmn = Pokemon()
pkmn.show()


