import xml.etree.ElementTree as ET
import requests
from flask import Flask
import batalha
import pokemon
import ataque

class Cliente:

	def __init__(self, execute = False):
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
			self.battle_state = requests.post('http://127.0.0.1:5000/battle/', data = xml).text
		except requests.exceptions.ConnectionError:
			print("Não foi possível conectar ao servidor.")
			return None
		pkmn2 = pokemon.lePokemonXML(1, self.battle_state)
		self.batalha = batalha.Batalha([pkmn, pkmn2])
		return self.atualizaBatalha()

	def atualizaBatalha(self):
		self.batalha.turno = 1
		root = ET.fromstring(self.battle_state)
		for i in range(0,2):
			pkmnXML = root[i]
			atksXML = root[i].findall('attacks')
			pkmn = self.batalha.pkmn[i]
			pkmn.setHpAtual(int(pkmnXML.find('attributes').find('health').text))

		self.batalha.display.pokemonHP(self.batalha.pkmn[1])
		self.batalha.display.pokemonHP(self.batalha.pkmn[0])

		if (not self.batalha.isOver()):
			self.batalha.turno = 0
			id = self.batalha.EscolheAtaque()
			self.batalha.pkmn[0].getAtks(id).decreasePp()
			self.battle_state = requests.post('http://127.0.0.1:5000/battle/attack/{}'.format(id + 1)).text
			self.atualizaBatalha()

		return 'FIM'


