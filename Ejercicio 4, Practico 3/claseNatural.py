from claseCalefactor import Calefactor

class Natural(Calefactor):
    def __init__(self,marca,modelo,matricula,calorias):
        super().__init__(marca,modelo)
        self.__matricula = matricula
        self.__calorias = int(calorias)
    def __str__(self):
        return 'Marca: %s Modelo: %s Matricula: %s Calorias: %skilocalorias/m3' % (super().getMarca(),super().getModelo(),self.__matricula,self.__calorias)

    def getMarca(self):
        return super().getMarca()
    def getModelo(self):
        return super().getModelo()
    def getMatricula(self):
        return self.__matricula
    def getCalorias(self):
        return self.__calorias
