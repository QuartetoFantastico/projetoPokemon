from flask import Flask
from flask import request
import xml.etree.ElementTree as ET
import batalha
import ataque
import pokemon

class Server:

	def __init__(self):
		self.app = Flask(__name__)
		self.app.debug = True
		self.battle_state = ''

		@self.app.route('/battle/', methods = ['GET' ,'POST'])
		def iniciaBatalha():
			if (request.method == 'GET'):
				return 'Hello World!'
			else:
				self.battle_state = self.criaBatalha('battle_state.xml')

				root = ET.fromstring(self.battle_state)
				hp = root[1].find('name').text
				print(hp)
				root[1].find('name').text = 'Raichu'
				res = ET.tostring(root)
				return res

		@self.app.route('/battle/attack/<id>')
		def hello_world2(id):
			return 'Hello World! {}'.format(id)

	def run(self):
		self.app.run()

	def lePokemonXML(self):

		tree = ET.parse(self.battle_state)
		root = tree.getroot()
		poke = root[0]
		atrib = []
		atrib.append(poke.find('name').text)
		atrib.append(int(poke.find('level').text))
		atrib.append(int(poke.find('attributes').find('health').text))
		atrib.append(int(poke.find('attributes').find('attack').text))
		atrib.append(int(poke.find('attributes').find('defense').text))
		atrib.append(int(poke.find('attributes').find('speed').text))
		atrib.append(int(poke.find('attributes').find('special').text))
		tipos = poke.findall('type')
		atrib.append(int(tipos[0].text))
		if (len(tipos) < 2): atrib.append(16)
		else: atrib.append(int(tipos[1].text))

		atks = [None, None, None, None]
		atqs = poke.findall('attacks')
		nAtks = len(atqs)
		for i in range(0, nAtks):
			atribAtk = []
			j = int(atqs[0].find('id').text) - 1
			atribAtk.append(atqs[0].find('name').text)
			atribAtk.append(int(atqs[0].find('type').text))
			atribAtk.append(int(atqs[0].find('power').text))
			atribAtk.append(int(atqs[0].find('accuracy').text))
			atribAtk.append(int(atqs[0].find('power_points').text))
			atks[j] = ataque.Ataque(atrib = atribAtk)

		struggle = ataque.Ataque(['Struggle', 0, 100, 50, 10])
		atks.append(struggle)	

		atrib.append(atks)
		pkmn = pokemon.Pokemon(atrib = atrib)
		return pkmn

	def criaBatalha(self):

		pokeServer = pokemon.Pokemon()
		tree = ET.parse(self.battle_state)
		root = tree.getroot()

		#Le o pokemon que já está no xml	
		pokeCliente = self.lePokemonXML()

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
			root[i].find('health').text = str(self.battle.pkmn[i].getHpAtual())
			atks = root[i].findall('attacks')
			for j in range(0, len(atks)):
				ind = int(atks[j].find('id').text) - 1
				atks[j].find('power_points').text = str(self.battle.pkmn[i].atks[ind].getPpAtual())

		return ET.tostring(root)

