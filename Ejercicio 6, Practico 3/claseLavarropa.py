from claseAparato import Aparato

class Lavarropa(Aparato):
    def __init__(self,marca,modelo,color,pais,precio,capLavado,velCentrifugado,cantProgramas,tipo):
        super().__init__(marca,modelo,color,pais,precio)
        self.__lavado = int(capLavado)
        self.__velocidad = velCentrifugado
        self.__cant = cantProgramas
        self.__tipo = tipo

    def __str__(self):
       return '%s %s %s %s %s %s %s %s %s' % (super().getMarca(),super().getModelo(),super().getColor(),super().getPais(),super().getPrecio(),self.__lavado,self.__velocidad,self.__cant,self.__tipo)

    def getTipo(self):
        return self.__tipo
    def getMarca(self):
        return super().getMarca()
    def getModelo(self):
        return super().getModelo()
    def getColor(self):
        return super().getColor()
    def getPais(self):
        return super().getPais()
    def getPrecio(self):
        return super().getPrecio()
    def mostrar(self):
        return '%s %s %s %s' % (self.__lavado, self.__velocidad, self.__cant, self.__tipo)

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = self.getMarca(),
                modelo = self.getModelo(),
                color = self.getColor(),
                pais = self.getPais(),
                precio = self.getPrecio(),
                cap = self.__lavado,
                vel = self.__velocidad,
                cant = self.__cant,
                tipo = self.__tipo,
            )
        )
        return d

    def calculo(self):
        total = self.getPrecio()
        if self.__lavado <= 5:
            total += (total * 1) / 100
        elif self.__lavado >= 5:
            total += (total * 3) / 100
        return total