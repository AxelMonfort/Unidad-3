from claseAparato import Aparato


class Televisor(Aparato):
    def __init__(self,marca,modelo,color,pais,precio,tipoPantalla,pulgadas,definicion,conexion):
        super().__init__(marca,modelo,color,pais,precio)
        self.__tipoPantalla = tipoPantalla
        self.__pulgadas = pulgadas
        self.__definicion = definicion
        self.__conexion = conexion

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (super().getMarca,super().getModelo,super().getColor,super().getPais,super().getPrecio,self.__tipoPantalla,self.__pulgadas,self.__definicion,self.__conexion)

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
        return ' %s %s %s %s' % (self.__tipoPantalla,self.__pulgadas,self.__definicion,self.__conexion)


    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = self.getMarca(),
                modelo = self.getModelo(),
                color = self.getColor(),
                pais = self.getPais(),
                precio = self.getPrecio(),
                pantalla = self.__tipoPantalla,
                pulgadas = self.__pulgadas,
                definicion = self.__definicion,
                conexion = self.__conexion
            )
        )
        return d

    def calculo(self):
        total = self.getPrecio()
        if self.__definicion == 'SD':
            total += (self.getPrecio() * 1) / 100
        elif self.__definicion == 'HD':
            total += (self.getPrecio() * 2) / 100
        elif self.__definicion == 'FULL HD':
            total += (self.getPrecio() * 3) / 100

        if self.__conexion == 'v':
            total += (self.getPrecio() * 10) / 100
        return total
