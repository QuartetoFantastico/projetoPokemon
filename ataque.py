class Ataque:

	def __init__(self):
		self._nome = ''
		self._typ = -1
		self._acu = -1
		self._pwr = -1
		self._pp = -1
		self._ppAtual = -1 

	def show(self):
		print('\tNome: {}'.format(self._nome))
		print('\tTipo: {}'.format(self._typ))
		print('\tAccuracy: {}'.format(self._acu))
		print('\tPower: {}'.format(self._pwr))
		print('\tPP: {}/{}'.format(self._ppAtual,self._pp))
		print()

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
