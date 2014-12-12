import xml.etree.ElementTree as ET
import requests
from flask import Flask
import batalha
import pokemon
import ataque

class Cliente:

	def __init__(self, execute = False, ip = '127.0.0.1', port = 5000, npc = False):
		self.ip = ip
		self.port = port
		self.npc = npc
		if (execute):
			self.iniciaBatalha()


	def writeXML(self, pkmn):
		#Escreve um XML a partir de um pokemon
		root = ET.Element('battle_state')
		ET.SubElement(root, "pokemon")
		poke = root.find('pokemon')

		ET.SubElement(poke, "name")
		poke.find('name').text = pkmn.getNome()

		ET.SubElement(poke, "level")
		poke.find('level').text = str(pkmn.getLvl())

		ET.SubElement(poke, "attributes")
		poke_att = poke.find('attributes')
		
		ET.SubElement(poke_att, "health")
		poke_att.find('health').text = str(pkmn.getHp())
		
		ET.SubElement(poke_att, "attack")
		poke_att.find('attack').text = str(pkmn.getAtk())
		
		ET.SubElement(poke_att, "defense")
		poke_att.find('defense').text = str(pkmn.getDefe())
		
		ET.SubElement(poke_att, "speed")
		poke_att.find('speed').text = str(pkmn.getSpd())
		
		ET.SubElement(poke_att, "special")
		poke_att.find('special').text = str(pkmn.getSpc())


		ET.SubElement(poke, "type")
		ET.SubElement(poke, "type")
		tipos = poke.findall('type')
		tipos[0].text = str(pkmn.getTyp1())
		tipos[1].text = str(pkmn.getTyp2())
		
		for i in range(0, 4):
			atk = pkmn.getAtks(i)
			if (atk is not None):
				ET.SubElement(poke, "attacks")
				poke_atk = poke.findall('attacks')

				ET.SubElement(poke_atk[-1], "id")
				poke_atk[-1].find('id').text = str(i + 1)

				ET.SubElement(poke_atk[-1], "name")
				poke_atk[-1].find('name').text = atk.getNome()
				
				ET.SubElement(poke_atk[-1], "type")
				poke_atk[-1].find('type').text = str(atk.getTyp())
				
				ET.SubElement(poke_atk[-1], "power")
				poke_atk[-1].find('power').text = str(atk.getPwr())
			
				ET.SubElement(poke_atk[-1], "accuracy")
				poke_atk[-1].find('accuracy').text = str(atk.getAcu())

				ET.SubElement(poke_atk[-1], "power_points")      
				poke_atk[-1].find('power_points').text = str(atk.getPpAtual())


		s = ET.tostring(root)
		return s

	def iniciaBatalha(self):
		pkmn = pokemon.Pokemon()
		xml = self.writeXML(pkmn)
		try:
			self.battle_state = requests.post('http://{}:{}/battle/'.format(self.ip, self.port), data = xml).text
		except requests.exceptions.ConnectionError:
			print("Não foi possível conectar ao servidor.")
			return None
		pkmn2 = pokemon.lePokemonXML(1, self.battle_state)
		self.batalha = batalha.Batalha([pkmn, pkmn2])
		if (self.npc): 
			self.batalha.pkmn[0].npc = True
			print("Eu sou um NPC")
		self.batalha.turno = 0
		self.batalha.display.showPokemon(self.batalha.pkmn[0])
		self.batalha.display.showPokemon(self.batalha.pkmn[1])
		return self.atualizaBatalha()

	def atualizaBatalha(self):
		self.batalha.AlternaTurno()
		root = ET.fromstring(self.battle_state)
		for i in range(0,2):
			pkmnXML = root[i]
			atksXML = root[i].findall('attacks')
			pkmn = self.batalha.pkmn[i]
			pkmn.setHpAtual(int(pkmnXML.find('attributes').find('health').text))

		self.batalha.showStatus()

		if (not self.batalha.isOver()):
			self.batalha.AlternaTurno()
			if (self.batalha.pkmn[self.batalha.turno].npc):
				id = self.batalha.EscolheAtaqueInteligente()
			else:
				id = self.batalha.EscolheAtaque()
			self.batalha.pkmn[0].getAtks(id).decreasePp()
			if (id == 4):
				self.battle_state = requests.post('http://{}:{}/battle/attack/{}'.format(self.ip, self.port, 0)).text
			else:
				self.battle_state = requests.post('http://{}:{}/battle/attack/{}'.format(self.ip, self.port, id + 1)).text
			self.simulaAtaque(id)
			self.atualizaBatalha()

		else: 
			self.batalha.showResults()

		return 'FIM'

	def sendShutdownSignal(self):
		requests.post('http://{}:{}/shutdown'.format(self.ip, self.port))

	def simulaAtaque(self, idCliente):
		disp = self.batalha.display
		root = ET.fromstring(self.battle_state)

		pkmnCXML = root[0]
		pkmnC = self.batalha.pkmn[0]

		pkmnSXML = root[1]
		pkmnS = self.batalha.pkmn[1]
		atksXML = pkmnSXML.findall('attacks')
		idServidor = self.descobreAtaqueUsado(atksXML, pkmnS)

		if (int(pkmnSXML.find('attributes').find('health').text) > 0):

			if (idCliente != 4):
				if (idServidor != 4):

					dmg = pkmnS.getHpAtual() - int(pkmnSXML.find('attributes').find('health').text)
					if (dmg == 0):
						disp.miss(pkmnC, pkmnS, pkmnC.getAtks(idCliente))
					else:
						disp.hit(pkmnC, pkmnS, pkmnC.getAtks(idCliente), dmg)

					dmg = pkmnC.getHpAtual() - int(pkmnCXML.find('attributes').find('health').text)
					if (dmg == 0):
						disp.miss(pkmnS, pkmnC, pkmnS.getAtks(idServidor))
					else:
						disp.hit(pkmnS, pkmnC, pkmnS.getAtks(idServidor), dmg)

				else:
					dmgStruggle = pkmnC.getHpAtual() - int(pkmnCXML.find('attributes').find('health').text)

					dmg = pkmnS.getHpAtual() - int(pkmnSXML.find('attributes').find('health').text) + round(dmgStruggle / 2, 0)
					if (dmg == 0):
						disp.miss(pkmnC, pkmnS, pkmnC.getAtks(idCliente))
					else:
						disp.hit(pkmnC, pkmnS, pkmnC.getAtks(idCliente), dmg)

					disp.hit(pkmnS, pkmnC, pkmnS.getAtks(idServidor), dmgStruggle)
					disp.hitSelf(pkmnS, round(dmgStruggle / 2, 0))

			else:
				if (idServidor != 4):
					dmgStruggle = pkmnS.getHpAtual() - int(pkmnSXML.find('attributes').find('health').text)

					disp.hit(pkmnC, pkmnS, pkmnC.getAtks(idCliente), dmgStruggle)
					disp.hitSelf(pkmnC, round(dmgStruggle / 2, 0))

					dmg = pkmnC.getHpAtual() - int(pkmnCXML.find('attributes').find('health').text) + round(dmgStruggle / 2, 0)
					if (dmg == 0):
						disp.miss(pkmnS, pkmnC, pkmnS.getAtks(idServidor))
					else:
						disp.hit(pkmnS, pkmnC, pkmnS.getAtks(idServidor), dmg)

				else:
					print('Ambos usam e se machucam com Struggle!')

		else:

			if (idCliente != 4):

				dmg = pkmnS.getHpAtual() - int(pkmnSXML.find('attributes').find('health').text)
				if (dmg == 0):
					disp.miss(pkmnC, pkmnS, pkmnC.getAtks(idCliente))
				else:
					disp.hit(pkmnC, pkmnS, pkmnC.getAtks(idCliente), dmg)

			else:
				dmgStruggle = pkmnC.getHpAtual() - int(pkmnCXML.find('attributes').find('health').text)

				disp.hit(pkmnC, pkmnS, pkmnC.getAtks(idServidor), dmgStruggle * 2)
				disp.hitSelf(pkmnC, round(dmgStruggle, 0))

	def descobreAtaqueUsado(self, atksXML, pkmn):
		for i in range(0, len(atksXML)):
			id = int(atksXML[i].find('id').text) - 1 
			ppXML = int(atksXML[i].find('power_points').text)
			pp = pkmn.getAtks(id).getPpAtual()

			if (pp != ppXML):
				pkmn.getAtks(id).decreasePp()
				return id

		return id







