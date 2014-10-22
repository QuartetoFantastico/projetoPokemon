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
		if (self.pkmn[0].spd > self.pkmn[1].spd):
			return 0
		elif (self.pkmn[1].spd > self.pkmn[0].spd):
			return 1
		return random.randint(0, 1)	

	def EscolheAtaque(self):
		number = int(input("Escolha o número do ataque\n"))
		return number

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
		if (atk.typ == self.pkmn[self.turno].typ1 or atk.typ == self.pkmn[self.turno].typ2): return 1.5
		return 1

	def CriticalHit(self):
		critical = (self.pkmn[self.turno].spd/512);
		temp = random.uniform(0, 1)
		if (temp <= critical):
			print("Critical Hit!")
			return (2 * self.pkmn[self.turno].lvl + 5)/(self.pkmn[self.turno].lvl+5)
		return 1

	def CalculaDano(self, atk):

		Critical = self.CriticalHit();
		tab = self.TypeChart('tabela.txt');
		STAB = self.StabBonus(atk)
		defending = (self.turno + 1) % 2
		Type = tab[atk.typ][self.pkmn[defending].typ1] * tab[atk.typ][self.pkmn[defending].typ2]
		Modifier = STAB * Type * Critical * random.uniform(0.85, 1)
		Damage = round(((2 * self.pkmn[self.turno].lvl + 10)/250 * self.pkmn[self.turno].atk/self.pkmn[defending].defe * atk.pwr + 2) * Modifier, 0);
		print("{} acerta {}! {} de dano ".format(self.pkmn[self.turno].nome, self.pkmn[defending].nome, Damage))
		return Damage


batalha = Batalha()
i = batalha.EscolheAtaque()
batalha.CalculaDano(batalha.pkmn[batalha.turno].atks[i])  