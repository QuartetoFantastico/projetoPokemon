from flask import Flask
from flask import request
import xml.etree.ElementTree as ET
app = Flask(__name__)

@app.route('/battle/', methods = ['GET' ,'POST'])
def hello_world():
	if (request.method == 'GET'):
		return 'Hello World!'
	else:
		tree = ET.parse('battle_state.xml')
		root = tree.getroot()
		hp = root[0].find('name').text
		print(hp)
		root[0].find('name').text = 'Raichu'
		res = ET.tostring(root)

		return res


@app.route('/battle/attack/<id>')
def hello_world2(id):
	return 'Hello World! {}'.format(id)

if __name__ == '__main__':
	app.debug = True
	app.run()