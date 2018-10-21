from beebotte import *

class BeebotteHandler():
    def __init__(self):
        self.api_key = 'QNMGqaXUTizwYJC7ly4rCswl'
        self.secret_key = 'hUVA4I7F76tIWIYW4qpx3jZRPdrxt7Sg'
        self.client = BBT(self.api_key, self.secret_key)
        self.channel = 'prueba'

    def InsertNew(self, New):

        print('\nComprobando Noticia\n')
        self.client.write(self.channel, 'Clics', New[0])
        self.client.write(self.channel, 'Meneos', New[1])
        self.client.write(self.channel, 'Noticia', New[2])
        self.client.write(self.channel, 'Fecha', New[3])
        self.client.write(self.channel, 'Hora', New[4])

        print('\nBase de Datos Beebotte\n')
        Clics = self.client.read(self.channel, 'Clics', 1000)
        Meneos = self.client.read(self.channel, 'Meneos', 1000)
        Noticia = self.client.read(self.channel, 'Noticia', 1000)
        Fecha = self.client.read(self.channel, 'Fecha', 1000)
        Hora = self.client.read(self.channel, 'Hora', 1000)

        print(Clics)
        print(Meneos)
        print(Noticia)
        print(Fecha)
        print(Hora)

        # for index, _ in enumerate(Clics):
        #     print('%d || %d || %s || %s || %s' % (Clics[index], Meneos[index], Noticia[index], Fecha[index], Hora[index]))