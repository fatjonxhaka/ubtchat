import mysql.connector
from abc import ABC , abstractmethod

class Database(ABC):

    @abstractmethod
    def dbcreate(self):
        pass

class DatabaseLink(Database):
    #krijimi i  funksionit per lidhje me mysqlserver-in

    def dbcreate(self, tup):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ubtchat"
        )
        self.cursor = self.connection.cursor()  
        try:
            self.cursor.execute("SELECT * FROM `ubtchatlist` WHERE `Perdoruesi`=%s AND `Fjalekalimi`=%s",tup)
            return (self.cursor.fetchone())
        except:
            return False
