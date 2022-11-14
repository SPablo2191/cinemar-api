import sqlite3 as sql
class db():
    def __init__(self,db):
        self.connection = sql.connect(db)
        self.cursor = self.connection.cursor()
    def query(self,query):
        """
            execute the query in sqlite database
        """
        self.cursor.execute(query)
    def commit(self):
        """
            confirm the query operation
        """
        self.connection.commit()
    def close(self):
        self.connection.close()