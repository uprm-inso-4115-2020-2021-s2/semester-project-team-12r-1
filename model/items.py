from config.dbconfig import pg_config
import psycopg2

class items:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host='localhost'" %(pg_config['dbname'], pg_config['user'],
                                                                  pg_config['password'], pg_config['dbport'])
        print("conection url:  ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getitems(self):
        cursor = self.conn.cursor()
        query = "select pitemid, items_names from items;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getitemById(self, pitemid):
        cursor = self.conn.cursor()
        query = "select pitemid, items_names from items where pitemid = %s;"

        cursor.execute(query, (pitemid))
        result = cursor.fetchone()
        return result

    def insertitem(self, items_names):
        cursor = self.conn.cursor()
        query = "insert into item ( pitemid, items_names) values(%s,%s)returning pitemid"
        cursor.execute(query, (items_names))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid


    def deleteitem(self, pitemid):
        cursor = self.conn.cursor()
        query = "delete from item where pitemid=%s;"
        cursor.execute(query,(pitemid))
        # determine affected rows
        affected_rows = cursor.rowcount
        self.conn.commit()
        # if affected rows == 0, the part was not found and hence not deleted
        # otherwise, it was deleted, so check if affected_rows != 0
        return affected_rows !=0