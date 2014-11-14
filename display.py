class Display:

	def __init__(self):
		self.display = True
		self.verbose = False

	def toggle(self):
		if (self.display): self.display = False
		else: self.display = True

	def toggleVerbose(self):
		if (self.verbose): self.verbose = False
		else: self.verbose = True
		print(self.verbose)

	def atkInvalido(self):
		if (self.display): print("\t\tAtaque inválido! Escolha outro ataque.")

	def ppInsuficiente(self):
		if (self.display): print("PP insuficiente, escolha outro ataque:")

	def listaAtaques(self, nAtks, l):
		if (self.display):
			for i in range(0, nAtks):
				print("{}. {} {}/{}".format(i + 1, l[i].getNome(), l[i].getPpAtual(), l[i].getPp()))
			print()

	def escolheAtaque(self, pkmn):
		if (self.display): 
			print("{}, escolha o ataque:".format(pkmn.getNome()))

	def criticalHit(self):
		if (self.display): print("Critical Hit!")

	def hit(self, atacando, defendendo, atk, Damage):
		if (self.display): print("{} acerta {} com {}! {} de dano ".format(atacando.getNome(), defendendo.getNome(), atk.getNome(), Damage))

	def miss(self, atacando, defendendo, atk):
		if (self.display): print("{} não acertou {} com {}!".format(atacando.getNome(), defendendo.getNome(), atk.getNome()))

	def hitSelf(self, atacando, Damage):
		if (self.display): print("{} se machuca! {} de dano ".format(atacando.getNome(), Damage))

	def pokemonHP(self, pkmn, left=True):
		if (self.display): 
			print("\n{} (Level {})".format(pkmn.getNome(), pkmn.getLvl()))
			print("[", end="")
			for i in range(0,20):
				if (0.05 * i < pkmn.getHpAtual() / pkmn.getHp()): print("|", end="")
				else: print(" ", end = "")
			print("]")
			print("HP: {}/{}\n".format(int(pkmn.getHpAtual()), int(pkmn.getHp())))

	def showPokemon(self, pkmn):
		if (self.verbose):
			print()
			print('Nome: {}'.format(pkmn.getNome()))
			print('Level: {}'.format(pkmn.getLvl()))
			print('HP: {}'.format(pkmn.getHp()))
			print('Ataque: {}'.format(pkmn.getAtk()))
			print('Defesa: {}'.format(pkmn.getDefe()))
			print('Speed: {}'.format(pkmn.getSpd()))
			print('Tipos: {} e {}'.format(pkmn.getTyp1(), pkmn.getTyp2()))
			print('Num Ataques: {}'.format(pkmn.getNatks()))
			print()
			print('Moves:')
			for i in range(0,4):
				if (pkmn.getAtks(i) is not None):
					self.showAtk(pkmn.getAtks(i))
				else: print('None')

	def showAtk(self, atk):
		if (self.verbose):
			print('\tNome: {}'.format(atk.getNome()))
			print('\tTipo: {}'.format(atk.getTyp()))
			print('\tAccuracy: {}'.format(atk.getAcu()))
			print('\tPower: {}'.format(atk.getPwr()))
			print('\tPP: {}/{}'.format(atk.getPpAtual(),atk.getPp()))
			print()
