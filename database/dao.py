from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_authorship():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT (role) 
                    FROM authorship
                    WHERE role!=''"""
        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_author(role):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT a.artist_id, a.name
                    FROM  artists a, authorship ars
                    wHERE ars.role=%s and ars.artist_id=a.artist_id
                    group by a.artist_id, a.name

                """
        cursor.execute(query,(role,))

        for row in cursor:
            result.append(Artist(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_connessioni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT as1.artist_id
                    FROM authorship as1, artists a1, objects o1
                    WHERE as1.artist_id=a1.artist_id and
                         o1.object_id=as1.object_id 
                        AND o1.curator_approved=1
                    group by as1.artist_id, as1.object_id
                """
        cursor.execute(query)

        for row in cursor:
            result.append((row['artist_id']))

        cursor.close()
        conn.close()
        return result