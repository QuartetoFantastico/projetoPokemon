import leitorpkmn
from sys import stdin
import xml.etree.ElementTree as ET
import ataque

class Pokemon:

	def __init__(self, atrib = ['', -1, -1, -1, -1, -1, -1, -1, -1, []]):
		if (len(atrib) < 10):
			print("Atributos faltando no Pokemon!!")
			while (len(atrib) < 10):
				atrib.append(-1)

		self._nome = atrib[0]
		self._lvl = atrib[1]
		self._hp = atrib[2]
		self._atk = atrib[3]
		self._defe = atrib[4]
		self._spd = atrib[5]
		self._spc = atrib[6]
		self._typ1 = atrib[7]
		self._typ2 = atrib[8]
		self._atks = atrib[9]
		self._hpAtual = atrib[2]
		self._struggle = 0

		if (self._lvl == -1):
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
		return self._struggle == 1

	def isAlive(self):
		return (self.getHpAtual() > 0)

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
	
	def setHpAtual(self, hp):
		if (hp < 0): hp = 0
		self._hpAtual = hp

	def setStruggle(self):
		struggle = 1
		for i in range(0, self.getNatks()):
			if (self.getAtks(i).ppCheck() != 0):
				struggle = 0	
		self._struggle = struggle
	
	def getAtkList(self):
		return self._atks

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

def lePokemonXML(i, battle_state):
	root = ET.fromstring(battle_state)
	poke = root[i]
	atrib = []
	atrib.append(poke.find('name').text)
	atrib.append(int(poke.find('level').text))
	atrib.append(int(poke.find('attributes').find('health').text))
	atrib.append(int(poke.find('attributes').find('attack').text))
	atrib.append(int(poke.find('attributes').find('defense').text))
	atrib.append(int(poke.find('attributes').find('speed').text))
	atrib.append(int(poke.find('attributes').find('special').text))
	tipos = poke.findall('type')
	atrib.append(int(tipos[0].text))
	if (len(tipos) < 2): atrib.append(16)
	else: atrib.append(int(tipos[1].text))

	atks = [None, None, None, None]
	atqs = poke.findall('attacks')
	nAtks = len(atqs)
	for i in range(0, nAtks):
		atribAtk = []
		j = int(atqs[i].find('id').text) - 1
		atribAtk.append(atqs[i].find('name').text)
		atribAtk.append(int(atqs[i].find('type').text))
		atribAtk.append(int(atqs[i].find('power').text))
		atribAtk.append(int(atqs[i].find('accuracy').text))
		atribAtk.append(int(atqs[i].find('power_points').text))
		atks[j] = ataque.Ataque(atrib = atribAtk)

	struggle = ataque.Ataque(['Struggle', 0, 100, 50, 10])
	atks.append(struggle)	

	atrib.append(atks)
	pkmn = Pokemon(atrib = atrib)
	return pkmn

