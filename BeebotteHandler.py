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
        Clics = self.client.read(self.channel, 'Clics', New[0])
        Meneos = self.client.read(self.channel, 'Meneos', New[1])
        Noticia = self.client.read(self.channel, 'Noticia', New[2])
        Fecha = self.client.read(self.channel, 'Fecha', New[3])
        Hora = self.client.read(self.channel, 'Hora', New[4])

        for index, _ in enumerate(Clics):
            print('%d || %d || %s || %s || %s' % (Clics[index], Meneos[index], Noticia[index], Fecha[index], Hora[index]))