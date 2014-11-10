from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/battle/')
def hello_world():
    return 'Hello World!'

@app.route('/battle/attack/<id>')
def hello_world2(id):
    return 'Hello World! {}'.format(id)

if __name__ == '__main__':
    app.run()