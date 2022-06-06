class Aparato:
    def __init__(self,marca,modelo,color,pais,precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__pais = pais
        self.__precioBase = int(precio)

    def str(self):
        return '%s %s %s %s %s' % (self.__marca,self.__modelo,self.__color,self.__pais,self.__precioBase)

    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getColor(self):
        return self.__color
    def getPais(self):
        return self.__pais
    def getPrecio(self):
        return self.__precioBase
    def mostrarAparato(self):
        return '%s %s %s %s %s' % (self.__marca, self.__modelo, self.__color, self.__pais, self.__precioBase)
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__=dict(
                marca = self.__marca,
                modelo = self.__modelo,
                color = self.__color,
                pais = self.__pais,
                precio = self.__precioBase,
            )
        )
        return d