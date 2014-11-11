from flask import Flask
from flask import request
import xml.etree.ElementTree as ET
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

def criaBattleState(battle_state):

	poke = pokemon.Pokemon()
	tree = ET.parse(battle_state)
	root = tree.getroot()

	pkmn = ET.SubElement(root, 'pokemon')

	aux = ET.SubElement(pkmn, 'name')
	aux.text = str(poke.getNome())

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
		aux.text = str(poke.getAtks(i).getNome())

		aux = ET.SubElement(atk, 'type')
		aux.text = str(poke.getAtks(i).getTyp())

		aux = ET.SubElement(atk, 'power')
		aux.text = str(poke.getAtks(i).getPwr())

		aux = ET.SubElement(atk, 'accuracy')
		aux.text = str(poke.getAtks(i).getAcu())

		aux = ET.SubElement(atk, 'power_points')
		aux.text = str(poke.getAtks(i).getPp())

	return ET.tostring(root)


@app.route('/battle/attack/<id>')
def hello_world2(id):
	return 'Hello World! {}'.format(id)

if __name__ == '__main__':
	app.debug = True
	app.run()