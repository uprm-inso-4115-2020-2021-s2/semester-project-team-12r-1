from flask import jsonify
from model.moves import movesDAO

class Moves: 

    def build_map_dict(self, row):
        result = {}
        result['move_id'] = row[0]
        result['move_type'] = row[1]
        result['move_base_power'] = row[2]
        result['secondary_effect'] = row[3]
        return result
    
    def build_attr_dict(self, move_id, move_type, move_base_power, secondary_effect):
        result = {}
        result['move_id'] = move_id
        result['move_type'] = move_type
        result['move_base_power'] = move_base_power
        result['secondary_effect'] = secondary_effect
        return result

    def getAllMoves(self):
        dao = movesDAO()
        moves_list = dao.getmoves()
        result_list = []
        for row in moves_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(moves_list)

    def getMoveId(self, pid):
        dao = movesDAO()
        move = dao.getmovesById(pid)
        if not move:
            return jsonify("Move not found"), 404
        else:
            result = self.build_map_dict(move)
            return jsonify(result)
    
    def newMove(self, json):
        move_type = json['move_type']
        move_base_power = json['move_base_power']
        secondary_effect = json['secondary_effect']
        dao = movesDAO()
        pid = dao.insertmove(move_type, move_base_power, secondary_effect)
        result = self.build_attr_dict(pid, move_type, move_base_power, secondary_effect)
        return jsonify(result), 201

    def deleteMove(self, pid):
        dao = movesDAO()
        result = dao.deleteMove(pid)
        if result:
            return jsonify("Move Deleted"), 200
        else:
            return jsonify("Move not found"), 404