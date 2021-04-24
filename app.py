from flask import Flask, jsonify, request
from flask_cors import CORS
from controller.basepokemon import BasePokemon

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

@app.route('/pokemons', methods=['GET'])
def users():
    if request.method == 'GET':
        return BasePokemon().getAllPokemon()
