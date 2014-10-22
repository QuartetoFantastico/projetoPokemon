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
		atacando = self.pkmn[self.turno]
		nAtks = atacando.getNatks()			

		if (atacando.isStruggling()):
			return 4

		else:
			print("Escolha o ataque:")
			while true:			
				for i in range(0, nAtks):
					print("{}. {} {}/{}".format(i + 1, atacando.getAtks(i).getNome(), atacando.getAtks(i).getPpAtual(), atacando.getAtks(i).getPp()))
				number = int(input(""))
				if (atacando.getAtks(number - 1).ppCheck()):
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
		return tab

	def StabBonus(self, atk):
		atacando = self.pkmn[self.turno]
		if (atk.getTyp() == atacando.getTyp1() or atk.getTyp() == atacando.getTyp2()): return 1.5
		return 1

	def CriticalHit(self):
		atacando = self.pkmn[self.turno]
		critical = (atacando.getSpd()/512);
		temp = random.uniform(0, 1)
		if (temp <= critical):
			print("Critical Hit!")
			return (2 * atacando.getLvl() + 5)/(atacando.getLvl() + 5)
		return 1

	def CalculaDano(self, atk):

		atacando = self.pkmn[self.turno]
		defendendo = self.pkmn[(self.turno + 1) % 2]
		Critical = self.CriticalHit();
		tab = self.TypeChart('tabela.txt');
		STAB = self.StabBonus(atk)

		Type = tab[atk.getTyp()][defendendo.getTyp1()] * tab[atk.getTyp()][defendendo.getTyp2()]
		Modifier = STAB * Type * Critical * random.uniform(0.85, 1)

		if (atk.isSpecial()):
			Damage = round(((2 * atacando.getLvl() + 10)/250 * atacando.getAtk() / defendendo.getDefe() * atk.getPwr() + 2) * Modifier, 0);
		else:
			Damage = round(((2 * atacando.getLvl() + 10)/250 * atacando.getSpc() / defendendo.getSpc() * atk.getPwr() + 2) * Modifier, 0);

		if (self.isHit(atk)):
			defendendo.setHpAtual(defendendo.getHpAtual() - Damage) 
			print("{} acerta {} com {}! {} de dano ".format(atacando.getNome(), defendendo.getNome(), atk.getNome(), Damage))
		else: print("{} não acertou {} com {}!".format(atacando.getNome(), defendendo.getNome(), atk.getNome()))

		if (atacando.isStruggling()):
			atacando.setHpAtual(atacando.getHpAtual() - Damage / 2) 
			print("{} se machuca! {} de dano ".format(atacando.getNome(), Damage / 2))

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

