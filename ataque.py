class Ataque:

	def __init__(self, atrib = ['', -1, -1, -1, -1]):
		if (len(atrib) < 5):
			print("Atributos faltando no Ataque!!")
			while (len(atrib) < 10):
				atrib.append(-1)

		self._nome = atrib[0]
		self._typ = atrib[1]
		self._pwr = atrib[2]
		self._acu = atrib[3]
		self._pp = atrib[4]
		self._ppAtual = atrib[4] 

	def ppCheck(self):
		return self._ppAtual > 0

	def setNome(self, nome):
		self._nome = nome

	def setTyp(self, typ):
		self._typ = typ

	def setAcu(self, acu):
		self._acu = acu

	def setPwr(self, pwr):
		self._pwr = pwr

	def setPp(self, pp):
		self._pp = pp
	
	def setPpAtual(self, ppAtual):
		self._ppAtual = ppAtual

	def getNome(self):
		return self._nome

	def getTyp(self):
		return self._typ

	def getAcu(self):
		return self._acu

	def getPwr(self):
		return self._pwr

	def getPp(self):
		return self._pp

	def getPpAtual(self):
		return self._ppAtual

	def decreasePp(self):
		if (self._nome is not 'Struggle'):
			self._ppAtual -= 1

	def isSpecial(self):
		return (self._typ >= 9 and self._typ != 16)
