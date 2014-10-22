import pokemon
import random

class Batalha:


	def __init__(self):
			self.pkmn = []
			self.pkmn.append(pokemon.Pokemon())
			self.pkmn[0].show()
			self.pkmn[0].setStruggle()
			self.pkmn.append(pokemon.Pokemon())
			self.pkmn[1].show()
			self.pkmn[1].setStruggle()
			self.turno = self.IniciaTurno()

	def IniciaTurno(self):
		if (self.pkmn[0].getSpd() > self.pkmn[1].getSpd()):
			return 0
		elif (self.pkmn[1].getSpd() > self.pkmn[0].getSpd()):
			return 1
		return random.randint(0, 1)	

	def AlternaTurno(self):
		self.pkmn[self.turno].setStruggle()
		self.turno = (self.turno + 1) % 2

	def EscolheAtaque(self):
		true = 1
		nAtks = self.pkmn[self.turno].getNatks()			

		if (self.pkmn[self.turno].isStruggling()):
			return 4

		else:
			print("Escolha o ataque:")
			while true:			
				for i in range(0, nAtks):
					print("{}. {} {}/{}".format(i + 1, self.pkmn[self.turno].getAtks(i).getNome(), self.pkmn[self.turno].getAtks(i).getPpAtual(), self.pkmn[self.turno].getAtks(i).getPp()))
				number = int(input(""))
				if (self.pkmn[self.turno].getAtks(number - 1).ppCheck()):
					return number - 1
				print("PP insuficiente, escolha outro ataque:")


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


		# for i in range(0, len(tab) - 1):
		# 	print(tab[i])	
		return tab


	def StabBonus(self, atk):
		if (atk.getTyp() == self.pkmn[self.turno].getTyp1() or atk.getTyp() == self.pkmn[self.turno].getTyp2()): return 1.5
		return 1

	def CriticalHit(self):
		critical = (self.pkmn[self.turno].getSpd()/512);
		temp = random.uniform(0, 1)
		if (temp <= critical):
			print("Critical Hit!")
			return (2 * self.pkmn[self.turno].getLvl() + 5)/(self.pkmn[self.turno].getLvl() + 5)
		return 1

	def CalculaDano(self, atk):

		Critical = self.CriticalHit();
		tab = self.TypeChart('tabela.txt');
		STAB = self.StabBonus(atk)
		defending = (self.turno + 1) % 2
		Type = tab[atk.getTyp()][self.pkmn[defending].getTyp1()] * tab[atk.getTyp()][self.pkmn[defending].getTyp2()]
		Modifier = STAB * Type * Critical * random.uniform(0.85, 1)
		Damage = round((((2 * self.pkmn[self.turno].getLvl() + 10)/250) * self.pkmn[self.turno].getAtk() /self.pkmn[defending].getDefe()  * atk.getPwr() + 2) * Modifier, 0);
		
		if (self.isHit(atk)):
			self.pkmn[defending].setHpAtual(self.pkmn[defending].getHpAtual() - Damage) 
			print("{} acerta {} com {}! {} de dano ".format(self.pkmn[self.turno].getNome(), self.pkmn[defending].getNome(), atk.getNome(), Damage))
		else: print("{} não acertou {} com {}!".format(self.pkmn[self.turno].getNome(), self.pkmn[defending].getNome(), atk.getNome()))

		if (self.pkmn[self.turno].isStruggling()):
			self.pkmn[self.turno].setHpAtual(self.pkmn[self.turno].getHpAtual() - Damage / 2) 
			print("{} se machuca! {} de dano ".format(self.pkmn[self.turno].getNome(), Damage / 2))


	def isHit(self, atk):
		x = random.uniform(0, 1)
		return x <= atk.getAcu() * 0.01

	def isOver(self):
		return not (self.pkmn[0].isAlive() and self.pkmn[1].isAlive())  


batalha = Batalha()
  
while (not batalha.isOver()):
	i = batalha.EscolheAtaque()
	batalha.pkmn[batalha.turno].getAtks(i).decreasePp()
	batalha.CalculaDano(batalha.pkmn[batalha.turno].getAtks(i))
	batalha.AlternaTurno()

if (not batalha.pkmn[0].isAlive() and not batalha.pkmn[1].isAlive()):
	print("Empate.")

elif (batalha.pkmn[0].isAlive()):
	print("{} ganhou!!".format(batalha.pkmn[0].getNome()))

else: print("{} ganhou!!".format(batalha.pkmn[1].getNome()))

