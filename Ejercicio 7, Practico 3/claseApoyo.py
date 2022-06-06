from clasePersonal import Personal

class Apoyo(Personal):
    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,categoria,area='',tipo='',clases=0,cargo='',catedra=''):
        super().__init__(cuil,apellido,nombre,sueldo,antiguedad,categoria,area,tipo,clases,cargo,catedra)
        self.__categoria = categoria

    def __str__(self):
        return '\nCategoria: %s'%(self.__categoria)

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

    def getCategoria(self):
        return self.__categoria

    def toJson(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil=self.getCuil(),
                apellido=self.getApellido(),
                nombre=self.getNombre(),
                sueldo=self.getSueldo(),
                antiguedad=self.getAntiguedad(),
                categoria=self.__categoria
            )
        )
        return d