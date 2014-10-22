import leitorpkmn
from sys import stdin

class Pokemon:

	def __init__(self):
		self._nome = ''
		self._lvl = -1
		self._hp = -1
		self._atk = -1
		self._defe = -1
		self._spd = -1
		self._spc = -1
		self._typ1 = -1
		self._typ2 = -1
		self._atks = []
		self._hpAtual = -1
		self._struggle = 0


		leitor = leitorpkmn.Leitor()
		lista = leitor.leitorDePokemons()
		if (len(lista) >= 10):
			self._nome = lista.pop(0)
			self._lvl = lista.pop(0)
			self._hp = lista.pop(0)
			self._atk = lista.pop(0)
			self._defe = lista.pop(0)
			self._spd = lista.pop(0)
			self._spc = lista.pop(0)
			self._typ1 =lista.pop(0)
			self._typ2 = lista.pop(0)
			self._hpAtual = self._hp
			lista.pop(0)
			while (len(lista) < 4):
				lista.append(None)
			self._atks = lista

	def isStruggling(self):
		return self._struggle

	def isAlive(self):
		return (self.getHpAtual() > 0)

	def show(self):
		print()
		print('Nome: {}'.format(self._nome))
		print('Level: {}'.format(self._lvl))
		print('HP: {}'.format(self._hp))
		print('Ataque: {}'.format(self._atk))
		print('Defesa: {}'.format(self._defe))
		print('Speed: {}'.format(self._spd))
		print('Tipos: {} e {}'.format(self._typ1, self._typ2))
		print('Num Ataques: {}'.format(self.getNatks()))
		print()
		print('Moves:')
		for i in range(0,4):
			if (self._atks[i] is not None):
				self._atks[i].show()

	def setNome(self, nome):
		self._nome = nome

	def setHp(self, hp):
		self._hp = hp

	def setAtk(self, atk):
		self._atk = atk

	def setDefe(self, defe):
		self._defe = defe

	def setSpd(self, spd):
		self._spd = spd

	def setSpc(self, spc):
		self._spc = spc

	def setTyp1(self, typ1):
		self._typ1 = typ1

	def setTyp2(self, typ2):
		self._typ2 = typ2

	def setAtks(self, i, atk):
		self._atks.append(atk)
	
	def setHpAtual(self, hp):
		self._hpAtual = hp

	def setStruggle(self):
		struggle = 1
		for i in range(0, self.getNatks()):
			if (self.getAtks(i).ppCheck() != 0):
				struggle = 0	
		self._struggle = struggle
	
	def getHp(self):
		return self._hp

	def getLvl(self):
		return self._lvl

	def getNome(self):
		return self._nome

	def getHp(self):
		return self._hp

	def getAtk(self):
		return self._atk

	def getDefe(self):
		return self._defe

	def getSpd(self):
		return self._spd

	def getSpc(self):
		return self._spc

	def getTyp1(self):
		return self._typ1

	def getTyp2(self):
		return self._typ2

	def getAtks(self, i):
		return self._atks[i]

	def getNatks(self):	
		cont = 0;
		for i in range(0,4):
			if self._atks[i] is not None:
				cont += 1
		return cont

	def getHpAtual(self):
		return self._hpAtual

