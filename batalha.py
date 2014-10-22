import pokemon
import random

class Batalha:


	def __init__(self):
			self.pkmn = []
			self.pkmn.append(pokemon.Pokemon())
			self.pkmn[0].show()
			self.pkmn.append(pokemon.Pokemon())
			self.pkmn[1].show()
			self.turno = self.IniciaTurno()

	def IniciaTurno(self):
		if (self.pkmn[0].getSpd() > self.pkmn[1].getSpd()):
			return 0
		elif (self.pkmn[1].getSpd() > self.pkmn[0].getSpd()):
			return 1
		return random.randint(0, 1)	

	def EscolheAtaque(self):
		print("Escolha o ataque:")
		for i in range(0, self.pkmn[self.turno].getNatks()):
			print("{}. {}".format(i + 1, self.pkmn[self.turno].getAtks(i).getNome()))
		number = int(input(""))
		return number - 1

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
		Damage = round(((2 * self.pkmn[self.turno].getLvl() + 10)/250 * self.pkmn[self.turno].getAtk() /self.pkmn[defending].getDefe()  * atk.getPwr() + 2) * Modifier, 0);
		print("{} acerta {} com {}! {} de dano ".format(self.pkmn[self.turno].getNome(), self.pkmn[defending].getNome(), atk.getNome(), Damage))


batalha = Batalha()
i = batalha.EscolheAtaque()
batalha.CalculaDano(batalha.pkmn[batalha.turno].getAtks(i))  