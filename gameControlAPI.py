from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import keyboard
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
endpoint = '/gameControl'

# http://localhost:5000/
@app.route(endpoint + '/moveRight', methods=['POST'])
def moveRight():
    keyboard.send('right')
    response = jsonify({'response': '200'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route(endpoint + '/moveLeft', methods=['POST'])
def moveLeft():
    keyboard.send('left')
    response = jsonify({'response': '200'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route(endpoint + '/moveDown', methods=['POST'])
def moveDown():
    keyboard.send('down')
    response = jsonify({'response': '200'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route(endpoint + '/moveUp', methods=['POST'])
def moveUp():
    keyboard.send('up')
    response = jsonify({'response': '200'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run()