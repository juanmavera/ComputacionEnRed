import numpy as np

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

        # print('\nComprobando Noticia\n')
        self.db.noticias.update_one({'Noticia': New[2]}, {'$set': entrada}, upsert=True) # si no hay match con la noticia la inserta

        # print('\nBase de Datos\n')
        # for doc in self.db.noticias.find():
        #     print(doc)

    def LeerNoticias(self):
        Clics = []
        Meneos = []
        Noticias = []
        Fechas = []
        Horas = []
        for New in self.db.noticias.find():
            Clics.append(int(float(New['Clics'])))
            Meneos.append(int(float(New['Meneos'])))
            Noticias.append(str(New['Noticia']))
            Fechas.append(str(New['Fecha']))
            Horas.append(str(New['Hora']))

        Clics = np.array(Clics)
        Meneos = np.array(Meneos)
        Noticias = np.array(Noticias)
        Fechas = np.array(Fechas)
        Horas = np.array(Horas)

        return Clics, Meneos, Noticias, Fechas, Horas