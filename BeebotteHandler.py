from beebotte import *

class BeebotteHandler():
    def __init__(self):
        self.api_key = 'QNMGqaXUTizwYJC7ly4rCswl'
        self.secret_key = 'hUVA4I7F76tIWIYW4qpx3jZRPdrxt7Sg'
        self.client = BBT(self.api_key, self.secret_key)
        self.channel = 'prueba'

    def InsertNew(self, New):

        self.client.write(self.channel, 'Clics', New[0])
        self.client.write(self.channel, 'Meneos', New[1])
        self.client.write(self.channel, 'Noticia', New[2])
        self.client.write(self.channel, 'Fecha', New[3])
        self.client.write(self.channel, 'Hora', New[4])


    def LeerNoticias(self):
        Clicsparcial = []
        Clics = []

        Meneosparcial = []
        Meneos = []

        Noticiasparcial = []
        Noticias = []

        Fechasparcial = []
        Fechas = []

        Horasparcial = []
        Horas = []

        TotalClics = self.client.read(self.channel, 'Clics', 1000)
        for clic in TotalClics:
            Clicsparcial.append(clic['data'])

        TotalMeneos = self.client.read(self.channel, 'Meneos', 1000)
        for meneo in TotalMeneos:
            Meneosparcial.append(meneo['data'])

        TotalNoticias = self.client.read(self.channel, 'Noticia', 1000)
        for noticia in TotalNoticias:
            Noticiasparcial.append(noticia['data'])

        TotalFechas = self.client.read(self.channel, 'Fecha', 1000)
        for fecha in TotalFechas:
            Fechasparcial.append(fecha['data'])

        TotalHoras = self.client.read(self.channel, 'Hora', 1000)
        for hora in TotalHoras:
            Horasparcial.append(hora['data'])

        print(len(Clicsparcial))
        print(len(Meneosparcial))
        print(len(Noticiasparcial))
        print(len(Fechasparcial))
        print(len(Horasparcial))

        for index in range(0, len(Noticiasparcial)-1):
            # print(index)
            if index == 0:
                NoticiaAux = Noticiasparcial[index]

            if NoticiaAux != Noticiasparcial[index]:

                print(NoticiaAux)
                print(Noticiasparcial[index - 1])
                print(Noticiasparcial[index])

                Clics.append(Clicsparcial[index - 1])
                Meneos.append(Meneosparcial[index - 1])
                Noticias.append(Noticiasparcial[index - 1])
                Fechas.append(Fechasparcial[index - 1])
                Horas.append(Horasparcial[index - 1])
                NoticiaAux = Noticiasparcial[index]

            Clics.append(Clicsparcial[len(Noticiasparcial) - 1])
            Meneos.append(Meneosparcial[len(Noticiasparcial) - 1])
            Noticias.append(Noticiasparcial[len(Noticiasparcial) - 1])
            Fechas.append(Fechasparcial[len(Noticiasparcial) - 1])
            Horas.append(Horasparcial[len(Noticiasparcial) - 1])

        return Clics, Meneos, Noticias, Fechas, Horas