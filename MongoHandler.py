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

        exists = self.db.noticias.find_one({'Noticia': New[2]})

        if exists is None:
            self.db.noticias.insert_one(entrada)
            print('Noticia Insertada')
        else:
            self.db.noticias.update_one({'Noticia': New[2]}, {'$inc': entrada})
            print('Noticia actualizada')

        for doc in self.db.noticias.find():
            print(doc)
