import leitorpkmn
from sys import stdin

class Pokemon:

	def __init__(self):
		self.nome = ''
		self.lvl = -1
		self.hp = -1
		self.atk = -1
		self.defe = -1
		self.spd = -1
		self.spc = -1
		self.typ1 =-1
		self.typ2 = -1
		self.atks = []


		leitor = leitorpkmn.Leitor()
		lista = leitor.leitorDePokemons()
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




