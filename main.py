import batalha
import sys
import cliente
import server
import globals

if (len(sys.argv) > 1):
	globals.init(1)
	if (sys.argv[1] == '-c' or sys.argv[1] == '-C'):
		c = cliente.Cliente(True)
		c.sendShutdownSignal()

	elif (sys.argv[1] == '-s' or sys.argv[1] == '-S'):
		s = server.Server()
		s.run()

else:

	intelig = 0
	batalha = batalha.Batalha()
	
	for i in range(0, len(sys.argv)):
		if (sys.argv[i] == '-s'): batalha.display.toggle()
		if (sys.argv[i] == '-v'): batalha.display.toggleVerbose()
		if (sys.argv[i] == '-i'): intelig = 1

	globals.init(intelig) 	

	batalha.display.showPokemon(batalha.pkmn[0])
	batalha.display.showPokemon(batalha.pkmn[1])

	while (not batalha.isOver()):
		# if (smart):
		# i = batalha.EscolheAtaqueInteligente()
		# else:
		i = batalha.EscolheAtaque()
		batalha.pkmn[batalha.turno].getAtks(i).decreasePp()
		batalha.CalculaDano(batalha.pkmn[batalha.turno].getAtks(i))
		batalha.showStatus()
		batalha.AlternaTurno()

	batalha.showResults()

	print("Pressione ENTER para sair")
