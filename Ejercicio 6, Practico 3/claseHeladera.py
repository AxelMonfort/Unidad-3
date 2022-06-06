from claseAparato import Aparato

class Heladera(Aparato):
    def __init__(self,marca,modelo,color,pais,precio,capacidadLitros,freezer,ciclico):
        super().__init__(marca,modelo,color,pais,precio)
        self.__capacidad = capacidadLitros
        self.__freezer = freezer
        self.__ciclico = ciclico

    def __str__(self):
        return '%s %s %s %s %s %s %s %s' % (super().getMarca,super().getModelo,super().getColor,super().getPais,super().getPrecio,self.__capacidad,self.__freezer,self.__ciclico)

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
        return '%s %s %s' % ( self.__capacidad,self.__freezer, self.__ciclico)

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = self.getMarca(),
                modelo = self.getModelo(),
                color = self.getColor(),
                pais = self.getPais(),
                precio = self.getPrecio(),
                capacidad = self.__capacidad,
                freezer = self.__freezer,
                ciclico = self.__ciclico,
            )
        )
        return d

    def calculo(self):
        total = self.getPrecio()
        if self.__freezer == 'f':
            total += (total * 1) / 100
        elif self.__freezer == 'v':
            total += (total*5) / 100
        if self.__ciclico == 'v':
            total += (total*10) / 100
        return total