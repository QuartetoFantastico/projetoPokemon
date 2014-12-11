import batalha
import sys
import cliente
import server

if (len(sys.argv) > 1 and (sys.argv[1] == '-s' or sys.argv[1] == '-S' or sys.argv[1] == '-c' or sys.argv[1] == '-C')):
	NPC = False
	if (len(sys.argv) > 2):
		NPC = (sys.argv[2] == '-i')
	if (sys.argv[1] == '-c' or sys.argv[1] == '-C'):
		c = cliente.Cliente(True, npc = NPC)
		c.sendShutdownSignal()

	elif (sys.argv[1] == '-s' or sys.argv[1] == '-S'):
		s = server.Server(npc = NPC)
		s.run()

	print("Pressione ENTER para sair")

else:

	batalha = batalha.Batalha()

	cont = 0
	for i in range(0, len(sys.argv)):
		if (sys.argv[i] == '-d'): batalha.display.toggle()
		if (sys.argv[i] == '-v'): batalha.display.toggleVerbose()
		if (sys.argv[i] == '-i'):
			if (cont < 2): batalha.pkmn[cont].npc = True
			print("Pokemon {} é um NPC".format(cont));
			batalha.pkmn[cont].npc = True
			cont += 1

	batalha.display.showPokemon(batalha.pkmn[0])
	batalha.display.showPokemon(batalha.pkmn[1])

	while (not batalha.isOver()):
		i = batalha.EscolheAtaque()
		batalha.pkmn[batalha.turno].getAtks(i).decreasePp()
		batalha.CalculaDano(batalha.pkmn[batalha.turno].getAtks(i))
		batalha.showStatus()
		batalha.AlternaTurno()

	batalha.showResults()

	print("Pressione ENTER para sair")
