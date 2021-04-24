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

@app.route('/pokemons', methods=['GET', 'POST'])
def pokemons():
    if request.method == 'POST':
        return BasePokemon().newPokemon(request.json)
    else:
        return BasePokemon().getAllPokemon()

@app.route('/pokemon/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def spec_pokemon(pid):
    if request.method == 'PUT':
        return BasePokemon().updatePokemon(request.json, pid)
    elif request.method == 'DELETE':
        return BasePokemon().deletePokemon(pid)
    else:
        return BasePokemon().getPokemonId(pid)