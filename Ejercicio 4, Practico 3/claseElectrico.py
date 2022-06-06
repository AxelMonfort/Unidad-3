from claseCalefactor import Calefactor

class Electrico(Calefactor):
    def __init__(self,marca,modelo,potencia):
        super().__init__(marca,modelo)
        self.__potencia = int(potencia)

    def __str__(self):
        return 'Marca: %s Modelo: %s Potencia: %sWatts' % (super().getMarca(),super().getModelo(),self.__potencia)

    def getMarca(self):
        return super().getMarca()
    def getModelo(self):
        return super().getModelo()
    def getPotencia(self):
        return self.__potencia