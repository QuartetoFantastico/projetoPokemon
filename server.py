from flask import Flask
from flask import request
import xml.etree.ElementTree as ET
import batalha
import ataque
import pokemon

app = Flask(__name__)

@app.route('/battle/', methods = ['GET' ,'POST'])
def iniciaBatalha():
	if (request.method == 'GET'):
		return 'Hello World!'
	else:
		battle_state = criaBattleState('battle_state.xml')

		root = ET.fromstring(battle_state)
		hp = root[1].find('name').text
		print(hp)
		root[1].find('name').text = 'Raichu'
		res = ET.tostring(root)

		return res

def lePokemonXML(battle_state):

	tree = ET.parse(battle_state)
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

def criaBattleState(battle_state):

	poke = pokemon.Pokemon()
	tree = ET.parse(battle_state)
	root = tree.getroot()

	#Le o pokemon que já está no xml	
	poke2 = lePokemonXML(battle_state)

	#Adiciona o outro pokemon ao xml
	pkmn = ET.SubElement(root, 'pokemon')

	aux = ET.SubElement(pkmn, 'name')
	aux.text = poke.getNome()

	aux = ET.SubElement(pkmn, 'level')
	aux.text = str(poke.getLvl())

	attributes = ET.SubElement(pkmn, 'attributes')
	aux = ET.SubElement(attributes, 'health')
	aux.text = str(poke.getHp())
	aux = ET.SubElement(attributes, 'attack')
	aux.text = str(poke.getAtk())
	aux = ET.SubElement(attributes, 'defense')
	aux.text = str(poke.getDefe())
	aux = ET.SubElement(attributes, 'speed')
	aux.text = str(poke.getSpd())
	aux = ET.SubElement(attributes, 'special')
	aux.text = str(poke.getSpc())

	aux = ET.SubElement(pkmn, 'type')
	aux.text = str(poke.getTyp1())

	aux = ET.SubElement(pkmn, 'type')
	aux.text = str(poke.getTyp2())

	for i in range(0, poke.getNatks()):
		atk = ET.SubElement(pkmn, 'attacks')

		aux = ET.SubElement(atk, 'id')
		x = i
		aux.text = str(x)

		aux = ET.SubElement(atk, 'name')
		aux.text = poke.getAtks(i).getNome()

		aux = ET.SubElement(atk, 'type')
		aux.text = str(poke.getAtks(i).getTyp())

		aux = ET.SubElement(atk, 'power')
		aux.text = str(poke.getAtks(i).getPwr())

		aux = ET.SubElement(atk, 'accuracy')
		aux.text = str(poke.getAtks(i).getAcu())

		aux = ET.SubElement(atk, 'power_points')
		aux.text = str(poke.getAtks(i).getPp())

	return ET.tostring(root)

def atualizaBattleState(battle_state):
	root = ET.fromstring(battle_state)
	pkmn1 = root[0]
	pkmn2 = root[1]

	


@app.route('/battle/attack/<id>')
def hello_world2(id):
	return 'Hello World! {}'.format(id)

if __name__ == '__main__':
	app.debug = True
	app.run()