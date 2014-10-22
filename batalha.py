import pokemon
import random

class Batalha:


	def __init__(self):
			self.pkmn = pokemon.Pokemon()
			self.pkmn.show()
			self.pkmn2 = pokemon.Pokemon()
			self.pkmn2.show()

	def IniciaTurno(self):
		if (self.pkmn.spd > self.pkmn2.spd):
			return self.pkmn
		elif (self.pkmn2.spd > self.pkmn.spd):
			return self.pkmn2
		else:
		    number = random.randint(1, 3)	
		    if (number == 1):
		    	return self.pkmn
		    else:
		    	return self.pkmn2

	def EscolheAtaque(self):
		number = int(input("Escolha o número do ataque"))
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


		for i in range(0, len(tab) - 1):
			print(tab[i])	
		return tab


	def StabBonus(self, atk):
		if (atk.typ == self.pkmn.typ1 or atk.typ == self.pkmn.typ2): return 1.5
		return 1

	def CriticalHit(self):
		critical = (self.pkmn.spd/512);
		temp = random.uniform(0, 1)
		if (temp <= critical):
			return (2 * self.pkmn.lvl + 5)/(self.pkmn.lvl+5)
		return 1

	def CalculaDano(self, atk):

		critical = self.CriticalHit();
		tab = self.TypeChart('tabela.txt');
		STAB = self.StabBonus(atk)
		Type = tab[atk.typ][self.pkmn2.typ1] * [atk.typ][self.pkmn2.typ2] 
		Modifier = STAB * Type * Critical * random.uniform(0.85, 1)
		Damage = ((2 * self.pkmn.lvl + 10)/250 * self.pkmn.atk/self.pkmn2.defe * atk.pwr + 2) * Modifier;
		print(Damage)


batalha = Batalha()
i = batalha.EscolheAtaque()
batalha.CalculaDano(batalha.pkmn.atks[i])  