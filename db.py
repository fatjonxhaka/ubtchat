import mysql.connector
from abc import ABC , abstractmethod

class Database(ABC):

    @abstractmethod
    def dbcreate(self):
        pass
