import fileinput
import re


class Batalha:

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
		if (atk.typ == pkmn.typ1 || atk.typ == pkmn.typ2) return 1.5
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
		Damage = (2 * pkmn.lvl + 10)/250 * pkmn.atk/pkmn2.defe * atk.pwr + 2) * Modifier;
		
class Pokemon:

	def __init__(self):
	

		cont = 0
		temp = fileinput.readline()
		if (temp is not None and cont <= 9):
			cont+= 1
			lista.append(temp)
			temp = fileinput.readline()
		
		for i in range (0, len(lista)- 1):
			pkmn.lista2[i] = leitorDeAtk()
		lista.append = lista2	

		for i in range(0, 8):
			pkmn.nome = lista.pop(obj=lista[0])
			pkmn.lvl = lista.pop(obj=lista[0])
			pkmn.hp = lista.pop(obj=lista[0])
			pkmn.atk = lista.pop(obj=lista[0])
			pkmn.defe = lista.pop(obj=lista[0])
			pkmn.spd = lista.pop(obj=lista[0])
			pkmn.typ1 = lista.pop(obj=lista[0])
			pkmn.typ2 = lista.pop(obj=lista[0])


	def isAlive(self):
		return (self.hpAtual > 0)

class Ataque:

	def __init__(self):
		atk.nome = atack_list.pop(obj=atack_list[0])
		atk.typ = atack_list.pop(obj=atack_list[0])
		atk.acu = atack_list.pop(obj=atack_list[0])
		atk.pwr = atack_list.pop(obj=atack_list[0])
		atk.pp = atack_list.pop(obj=atack_list[0])





class Leitor:

	# def leitorDePokemon(self):

		

	# 	return pkmn = Pokemon()
	# 	pkmn = Pokemon()

	def leitorDeAtk(self):

		atk = Ataque()
		atack_list = []
		for i in range(0,4):
			atack_list.append = fileinput.readline() 
		
		return atack_list



# leitor = Leitor()
# pkmn = leitor.leitorDePokemon()
# pkmn2 = leitor.leitorDePokemon()


battle = Batalha()
battle.TypeChart('tabela.txt')    

