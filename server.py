from flask import Flask
from flask import request
import xml.etree.ElementTree as ET
import batalha
import ataque
import pokemon
import display

class Server:

	def __init__(self):
		self.app = Flask(__name__)
		self.app.debug = True
		self.battle_state = ''

		@self.app.route('/battle/', methods = ['GET' ,'POST'])
		def iniciaBatalha():
			if (request.method == 'POST'):
				self.battle_state = self.criaBatalha(request.data)

				if (self.batalha.turno == 0):
					i = self.batalha.EscolheAtaque()
					self.batalha.pkmn[0].getAtks(i).decreasePp()
					self.batalha.CalculaDano(self.batalha.pkmn[0].getAtks(i))
					self.battle_state = self.atualizaBattleState()

				return self.battle_state
			else:
				return 'Hello World!'

		@self.app.route('/battle/attack/<id>', methods = ['GET' ,'POST'])
		def recebeAtaque(id):
			if (request.method == 'POST'):
				self.batalha.pkmn[1].getAtks(int(id) - 1).decreasePp()
				self.batalha.CalculaDano(self.batalha.pkmn[1].getAtks(int(id) - 1))
				self.batalha.AlternaTurno()

				self.batalha.display.pokemonHP(self.batalha.pkmn[0])
				self.batalha.display.pokemonHP(self.batalha.pkmn[1])

				i = self.batalha.EscolheAtaque()
				self.batalha.pkmn[1].getAtks(i).decreasePp()
				self.batalha.CalculaDano(self.batalha.pkmn[1].getAtks(i))
				self.battle_state = self.atualizaBattleState()
				self.batalha.AlternaTurno()
				return self.battle_state
			else:
				return 'Hello World! {}'.format(id)

	def run(self):
		self.app.run()

	def criaBatalha(self, battle_state):

		pokeServer = pokemon.Pokemon()
		root = ET.fromstring(battle_state)

		#Le o pokemon que já está no xml	
		pokeCliente = pokemon.lePokemonXML(0, battle_state)

		#Adiciona o outro pokemon ao xml
		pkmn = ET.SubElement(root, 'pokemon')

		aux = ET.SubElement(pkmn, 'name')
		aux.text = pokeServer.getNome()

		aux = ET.SubElement(pkmn, 'level')
		aux.text = str(pokeServer.getLvl())

		attributes = ET.SubElement(pkmn, 'attributes')
		aux = ET.SubElement(attributes, 'health')
		aux.text = str(pokeServer.getHp())
		aux = ET.SubElement(attributes, 'attack')
		aux.text = str(pokeServer.getAtk())
		aux = ET.SubElement(attributes, 'defense')
		aux.text = str(pokeServer.getDefe())
		aux = ET.SubElement(attributes, 'speed')
		aux.text = str(pokeServer.getSpd())
		aux = ET.SubElement(attributes, 'special')
		aux.text = str(pokeServer.getSpc())

		aux = ET.SubElement(pkmn, 'type')
		aux.text = str(pokeServer.getTyp1())

		aux = ET.SubElement(pkmn, 'type')
		aux.text = str(pokeServer.getTyp2())

		for i in range(0, pokeServer.getNatks()):
			atk = ET.SubElement(pkmn, 'attacks')

			aux = ET.SubElement(atk, 'id')
			x = i
			aux.text = str(x)

			aux = ET.SubElement(atk, 'name')
			aux.text = pokeServer.getAtks(i).getNome()

			aux = ET.SubElement(atk, 'type')
			aux.text = str(pokeServer.getAtks(i).getTyp())

			aux = ET.SubElement(atk, 'power')
			aux.text = str(pokeServer.getAtks(i).getPwr())

			aux = ET.SubElement(atk, 'accuracy')
			aux.text = str(pokeServer.getAtks(i).getAcu())

			aux = ET.SubElement(atk, 'power_points')
			aux.text = str(pokeServer.getAtks(i).getPp())
 
		self.batalha = batalha.Batalha([pokeServer, pokeCliente])

		return ET.tostring(root)

	def atualizaBattleState(self):
		root = ET.fromstring(self.battle_state)

		for i in range(0, 2):
			root[i].find('attributes').find('health').text = str(self.batalha.pkmn[i].getHpAtual())
			atks = root[i].findall('attacks')
			for j in range(0, len(atks)):
				ind = int(atks[j].find('id').text) - 1
				atks[j].find('power_points').text = str(self.batalha.pkmn[i].getAtks(ind).getPpAtual())

		self.batalha.display.pokemonHP(self.batalha.pkmn[0])
		self.batalha.display.pokemonHP(self.batalha.pkmn[1])

		return ET.tostring(root)

