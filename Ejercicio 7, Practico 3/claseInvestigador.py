from clasePersonal import Personal

class Investigador(Personal):
    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,area,tipo,categoria='',clases=0,cargo='',catedra=''):
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad, categoria, area, tipo, clases, cargo, catedra)
        self.__area = area
        self.__tipo = tipo

    def __str__(self):
        return '\nArea: %s  Tipo: %s'%(self.__area,self.__tipo)

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

    def getArea(self):
        return self.__area
    def getTipo(self):
        return self.__tipo

    def toJson(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__=dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldo=self.getSueldo(),
                antiguedad=self.getAntiguedad(),
                area=self.__area,
                tipo=self.__tipo
            )
        )
        return d