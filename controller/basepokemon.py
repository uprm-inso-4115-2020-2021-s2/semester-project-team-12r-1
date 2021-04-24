from flask import jsonify
from model.basepokemon import BasePokemonDAO

class BasePokemon: 

    def build_map_dict(self, row):
        result = {}
        result['p_id'] = row[0]
        result['p_name'] = row[1]
        result['ptype1'] = row[2]
        result['ptype2'] = row[3]
        result['base_hp'] = row[4]
        result['base_atk'] = row[5]
        result['base_def'] = row[6]
        result['base_spatk'] = row[7]
        result['base_spdef'] = row[8]
        result['base_spd'] = row[9]
        return result
    
    def build_atrr_dict(self, pid, pname, ptype1, ptype2, bhp, batk, bdef, bspatk, bspdef, bspd):
        result = {}
        result['p_id'] = pid
        result['p_name'] = pname
        result['ptype1'] = ptype1
        result['ptype2'] = ptype2
        result['base_hp'] = bhp
        result['base_atk'] = batk
        result['base_def'] = bdef
        result['base_spatk'] = bspatk
        result['base_spdef'] = bspdef
        result['base_spd'] = bspd
        return result

    def getAllPokemon(self):
        dao = BasePokemonDAO()
        pokemon_list = dao.getAllPokemon
        result_list = []
        for row in pokemon_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(pokemon_list)