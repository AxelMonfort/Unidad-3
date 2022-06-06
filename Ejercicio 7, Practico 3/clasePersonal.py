class Personal:
    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,clases=0,cargo='',catedra='',categoria='',area='',tipo=''):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldo = int(sueldo)
        self.__antiguedad = int(antiguedad)

    def __str__(self):
        cadena = print('\nDATOS PERSONAL.')
        cadena += print('\nCUIL: '+str(self.__cuil)+'   Apellido: '+str(self.__apellido)+'  Nombre: '+str(self.__nombre))
        cadena +=print('\nSUELDO: %s'%(self.__sueldo))
        cadena +=print('\nANTIGUEDAD: %s'%(self.__antiguedad))
        return cadena

    def getCuil(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getSueldo(self):
        return self.__sueldo
    def getAntiguedad(self):
        return self.__antiguedad


    def toJson(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = self.__cuil,
                apellido = self.__apellido,
                nombre = self.__nombre,
                sueldo = self.__sueldo,
                antiguedad = self.__antiguedad
            )
        )
        return d
