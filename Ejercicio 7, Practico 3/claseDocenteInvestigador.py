from claseDocente import Docente
from claseInvestigador import Investigador

class DocenteInvestigador(Docente,Investigador):
    def __init__(self,cuil,apellido,nombre,sueldo,antiguedad,area,tipo,clases,cargo,catedra,categoriaD,importe,categoria=''):
        super().__init__(cuil,apellido,nombre,sueldo,antiguedad,categoria,area,tipo,clases,cargo,catedra)
        self.__categoriaD = categoriaD
        self.__importe = importe

    def __str__(self):
        return '\nCategoria: %s  Importe: $%s'%(self.__categoriaD,self.__importe)

    def getCategoriaD(self):
        return self.__categoriaD
    def getImporte(self):
        return self.__importe

    def toJson(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = super().getCuil(),
                apellido = super().getApellido(),
                nombre = super().getNombre(),
                sueldo = super().getSueldo(),
                antiguedad = super().getAntiguedad(),
                clases = super().getClases(),
                cargo = super().getCargo(),
                catedra = super().getCatedra(),
                area = super().getArea(),
                tipo = super().getTipo(),
                categoriaD=self.__categoriaD,
                importe=self.__importe
            )
        )
        return d