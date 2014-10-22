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
		self.typ1 = -1
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

	def setHp(self, hp):
		self.Hp = hp

	def setNome(self, nome):
		self.nome = nome

	def setHp(self, hp):
		self.Hp = hp

	def setAtk(self, atk):
		self.atk = atk

	def setDefe(self, defe):
		self.defe = defe

	def setSpd(self, spd):
		self.spd = spd

	def setSpc(self, spc):
		self.spc = spc

	def setTyp1(self, typ1):
		self.typ1 = typ1

	def setTyp2(self, typ2):
		self.typ2 = typ2

	def getHp(self):
		return self.hp

	def getLvl(self):
		return self.lvl

	def getNome(self):
		return self.nome

	def getHp(self):
		return self.Hp

	def getAtk(self):
		return self.atk

	def getDefe(self):
		return self.defe

	def getSpd(self):
		return self.spd

	def getSpc(self):
		return self.spc

	def getTyp1(self):
		return self.typ1

	def getTyp2(self):
		return self.typ2


