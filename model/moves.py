from config.dbconfig import pg_config
import psycopg2

class movesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" %(pg_config['dbname'], pg_config['user'],
                                                                  pg_config['password'], pg_config['dbport'], pg_config['host'])
        print("conection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getmoves(self):
        cursor = self.conn.cursor()
        query = "select move_id,move_name, move_type, move_basepower, secondary_effect from moves;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getmovebyid(self, move_id):
        cursor = self.conn.cursor()
        query = "select move_id,move_name, move_type, move_basepower, secondary_effect from moves where move_id = %s;"

        cursor.execute(query, (move_id))
        result = cursor.fetchone()
        return result

    def insertmove(self,move_name, move_type, move_basepower, secondary_effect):
        cursor = self.conn.cursor()
        query = "insert into moves ( move_name, move_type, move_basepower, secondary_effect) values(%s,%s,%s,%s)returning move_id"
        cursor.execute(query, (move_name, move_type, move_basepower, secondary_effect))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def deleteitem(self, move_id):
        cursor = self.conn.cursor()
        query = "delete from moves where move_id=%s;"
        cursor.execute(query,(move_id))
        # determine affected rows
        affected = cursor.rowcount
        self.conn.commit()
        # if affected rows == 0, the part was not found and hence not deleted
        # otherwise, it was deleted, so check if affected_rows != 0
        return affected !=0