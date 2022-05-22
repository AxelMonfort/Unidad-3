class Flor:
    def __init__(self,nro,nom,color,descripcion):
        self.__nro = nro
        self.__nom = nom
        self.__color = color
        self.__descripcion = descripcion
        self.__cont = 0

    def __str__(self):
        return 'nro %s  nombre %s  color %s  descripcion %s  cantidad %s' % (self.__nro,self.__nom,self.__color,self.__descripcion,self.__cont)

    def getNom(self):
        return self.__nom

    def contar(self):
        self.__cont += 1

    def getCont(self):
        return self.__cont

    def __gt__(self, other):
        return self.__cont < other.__cont