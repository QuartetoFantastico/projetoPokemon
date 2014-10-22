import pokemon

class Batalha:

	def IniciaTurno(self):
		if (pkmn.spd > pkmn2.spd):
			return pkmn
		elif (pkmn2.spd > pkmn.spd):
			return pkmn2
		else:
		    number = random.randint(1, 3)	
		    if (number == 1):
		    	return pkmn
		    else:
		    	return pkmn2

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


	def StabBonus():
		if (atk.typ == pkmn.typ1 or atk.typ == pkmn.typ2): return 1.5
		return 1

	def CriticalHit():
		critical = (pkmn.spd/512);
		temp = random.uniform(0, 1)
		if (temp <= critical):
			return (2 * pkmn.lvl + 5)/(pkmn.lvl+5)
		return 1

	def CalculaDano(self, atk):

		critical = CriticalHit();
		tab = TypeChart();
		STAB = StabBonus()
		Type = tab[atk.typ][pkmn2.typ1] * [atk.typ][pkmn2.typ2] 
		Modifier = STAB * Type * Critical * random.uniform(0.85, 1)
		Damage = ((2 * pkmn.lvl + 10)/250 * pkmn.atk/pkmn2.defe * atk.pwr + 2) * Modifier;


pkmn = pokemon.Pokemon()
pkmn.show()
