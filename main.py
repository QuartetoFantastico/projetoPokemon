import batalha
import sys
import cliente
import server

if (sys.argv[1] == '-c' || sys.argv[1] == '-C'):
	c = cliente.Cliente(True)

elif (sys.argv[1] == '-s' || sys.argv[1] == '-S'):
	s = server.Server()

else:

	batalha = batalha.Batalha()

	for i in range(0, len(sys.argv)):
		if (sys.argv[i] == '-s'): batalha.display.toggle()
		if (sys.argv[i] == '-v'): batalha.display.toggleVerbose()

	batalha.display.showPokemon(batalha.pkmn[0])
	batalha.display.showPokemon(batalha.pkmn[1])

	while (not batalha.isOver()):
		i = batalha.EscolheAtaque()
		batalha.pkmn[batalha.turno].getAtks(i).decreasePp()
		batalha.CalculaDano(batalha.pkmn[batalha.turno].getAtks(i))
		batalha.display.pokemonHP(batalha.pkmn[0])
		batalha.display.pokemonHP(batalha.pkmn[1])
		batalha.AlternaTurno()

	if (not batalha.pkmn[0].isAlive() and not batalha.pkmn[1].isAlive()):
		print("Empate.")

	elif (batalha.pkmn[0].isAlive()):
		print("{} ganhou!!".format(batalha.pkmn[0].getNome()))

	else: print("{} ganhou!!".format(batalha.pkmn[1].getNome()))

	print("Pressione ENTER para sair")
