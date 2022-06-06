from clasePersonal import Personal

class Docente(Personal):
    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,clases,cargo,catedra,categoria='',area='',tipo='',):
        super().__init__(cuil,apellido,nombre,sueldo,antiguedad,clases,cargo,catedra)
        self.__clases = clases
        self.__cargo = cargo
        self.__catedra = catedra

    def __str__(self):
        return '\nClases: %s  Cargo: %s  Catedra: %s'%(self.__clases,self.__cargo,self.__catedra)

    def getCuil(self):
        return super().getCuil()
    def getApellido(self):
        return super().getApellido()
    def getNombre(self):
        return super().getNombre()
    def getSueldo(self):
        return super().getSueldo()
    def getAntiguedad(self):
        return super().getAntiguedad()

    def getClases(self):
        return self.__clases
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra


    def toJson(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldo=self.getSueldo(),
                antiguedad=self.getAntiguedad(),
                clases=self.__clases,
                cargo=self.__cargo,
                catedra=self.__catedra
            )
        )
        return d