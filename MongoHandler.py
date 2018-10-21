from pymongo import MongoClient


class MongoHandler():
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.prueba

    def InsertNew(self, New):

        entrada = {
            'Clics': New[0],
            'Meneos': New[1],
            'Noticia': New[2],
            'Fecha': New[3],
            'Hora': New[4]
        }

        self.db.noticias.insert_one(entrada)
