class Jugador:
    def __init__(self,nombre,dni,ciudad,pais,fechaNacimiento):
        self.__nombre = nombre
        self.__dni = dni
        self.__ciudad = ciudad
        self.__pais = pais
        self.__fecha = fechaNacimiento

    def __str__(self):
        return 'Nombre: %s DNI: %s Ciudad: %s Pais: %s Fecha: %s' % (self.__nombre,self.__dni,self.__ciudad,self.__pais,self.__fecha)

    def getNombre(self):
        return self.__nombre
    def getDNI(self):
        return self.__dni
    def getCiudad(self):
        return self.__ciudad