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
