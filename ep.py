import fileinput
import re


class Batalha:

	Damage = (2 * pkmn.lvl + 10)/250 * Attack/Defense * Base + 2) * Modifier;
	Modifier = STAB * Type * Critical * other * random.uniform(0.85, 1)

class Pokemon:

	def __init__(self):
	
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

	def leitorDePokemon(self):

		cont = 0
		if ((temp = fileinput.readline() is not None) and cont <= 9):
			cont+= 1
			lista.append(temp)
		
		for i in range (0, len(lista)- 1):
			pkmn.lista2[i] = leitorDeAtk()
		lista.append = lista2	

		pkmn = Pokemon()


	def leitorDeAtk(self):

		atk = Ataque()
		atack_list = []
		for i in range(0,4):
			atack_list.append = fileinput.readline() 
		
		return atack_list



leitor = Leitor()
leitor.leitorDePokemon()
	    

