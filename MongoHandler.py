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

        print('\nComprobando Noticia\n')
        self.db.noticias.update_one({'Noticia': New[2]}, {'$set': entrada}, upsert=True) # si no hay match con la noticia la inserta

        print('\nBase de Datos\n')
        for doc in self.db.noticias.find():
            print(doc)
