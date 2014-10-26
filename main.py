import batalha

batalha = batalha.Batalha()
  
while (not batalha.isOver()):
	i = batalha.EscolheAtaque()
	batalha.pkmn[batalha.turno].getAtks(i).decreasePp()
	batalha.CalculaDano(batalha.pkmn[batalha.turno].getAtks(i))
	print("\n{} (Level {}): {} de hp".format(batalha.pkmn[0].getNome(), batalha.pkmn[0].getLvl(), int(batalha.pkmn[0].getHpAtual())))
	print("{} (Level {}): {} de hp \n".format(batalha.pkmn[1].getNome(), batalha.pkmn[1].getLvl(), int(batalha.pkmn[1].getHpAtual())))
	batalha.AlternaTurno()

if (not batalha.pkmn[0].isAlive() and not batalha.pkmn[1].isAlive()):
	print("Empate.")

elif (batalha.pkmn[0].isAlive()):
	print("{} ganhou!!".format(batalha.pkmn[0].getNome()))

else: print("{} ganhou!!".format(batalha.pkmn[1].getNome()))

print("Pressione ENTER para sair")
