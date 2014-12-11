import pokemon
import random
import re
import display

class Batalha:

	def __init__(self, pokeList = []):
		self.display = display.Display()
		self.pkmn = []
		if (len(pokeList) == 0): 
			self.pkmn.append(pokemon.Pokemon())
			self.pkmn.append(pokemon.Pokemon())
		else:
			self.pkmn = pokeList
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
		atacando = self.pkmn[self.turno]
		nAtks = atacando.getNatks()	
		escolheu = 0		

		if (atacando.isStruggling()):
			print("I am struggling....")
			return 4

		else:
			if (atacando.npc):
				x = self.EscolheAtaqueInteligente()
				print ("{} escolhe o ataque {}".format(atacando.getNome(),x))
				return x

			else:
				self.display.escolheAtaque(atacando)
				while True:			
					self.display.listaAtaques(nAtks, atacando.getAtkList())
					while (not escolheu):
						number = input("")
						p = re.compile('[0-9]')
						if (p.match(number)):
							number = int(number)
							if (number > nAtks or number < 1):
								self.display.atkInvalido()
							else: escolheu = 1
							if (escolheu):
								if (atacando.getAtks(number - 1).ppCheck()):
									return number - 1
								self.display.ppInsuficiente()
								escolheu = 0
						else: self.display.atkInvalido()

	def EscolheAtaqueInteligente(self):
		#Para maximizar o dano, deve-se maximizar a Base X Tipo X STAB
		true = 1
		tab = self.TypeChart('tabela.txt')
		atacando = self.pkmn[self.turno]
		defendendo = self.pkmn[(self.turno + 1) % 2]
		BaseXType = 0
		lista = atacando.getAtkList()
		TypeMaior = tab[lista[0].getTyp()][defendendo.getTyp1()] * tab[lista[0].getTyp()][defendendo.getTyp2()]

		if (defendendo.getHpAtual() < 100):
			for i in range(0, atacando.getNatks() - 1):
				print("i = {}".format(i))
				Type = tab[lista[i].getTyp()][defendendo.getTyp1()] * tab[lista[i].getTyp()][defendendo.getTyp2()]
				atual = lista[i].getPwr() * Type * (lista[i].getAcu()/100) * self.StabBonus(lista[i])
				maior = lista[BaseXType].getPwr() * TypeMaior * (lista[BaseXType].getAcu()/100) * self.StabBonus(lista[BaseXType])
				if (atual > maior):
					BaseXType = i
					TypeMaior = Type
		else:	
			for i in range(0, atacando.getNatks() - 1):
				print("i = {}".format(i))
				Type = tab[lista[i].getTyp()][defendendo.getTyp1()] * tab[lista[i].getTyp()][defendendo.getTyp2()]
				atual = lista[i].getPwr() * Type * self.StabBonus(lista[i])
				maior = lista[BaseXType].getPwr() * TypeMaior * self.StabBonus(lista[BaseXType])
				if (atual > maior):
					BaseXType = i
					TypeMaior = Type
		print(BaseXType)
		return BaseXType

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
		arquivo.close()
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
			self.display.criticalHit()
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
			defendendo.setHpAtual(int(defendendo.getHpAtual() - Damage))
			self.display.hit(atacando, defendendo, atk, Damage)
		else: self.display.miss(atacando, defendendo, atk)

		if (atacando.isStruggling()):
			Damage = round(Damage / 2, 0)
			atacando.setHpAtual(int(atacando.getHpAtual() - Damage))
			self.display.hitSelf(atacando, Damage)

	def isHit(self, atk):
		x = random.uniform(0, 1)
		return x <= atk.getAcu() * 0.01

	def isOver(self):
		return not (self.pkmn[0].isAlive() and self.pkmn[1].isAlive())

	def showResults(self):
		if (not self.pkmn[0].isAlive() and not self.pkmn[1].isAlive()):
			self.display.showTie()

		elif (self.pkmn[0].isAlive()):
			self.display.showWinner(self.pkmn[0])

		else: self.display.showWinner(self.pkmn[1])

	def showStatus(self):
		self.display.pokemonHP(self.pkmn[1])
		self.display.pokemonHP(self.pkmn[0])
