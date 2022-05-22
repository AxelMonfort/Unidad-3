class Carrera:
    def __init__(self,codigo,nombre,duracion,titulo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion


    def __str__(self):
        return '\n\tCodigo: %s  Nombre: %s  Duracion: %s  Titulo: %s' % (self.__codigo,self.__nombre,self.__titulo,self.__duracion)

    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getDuracion(self):
        return self.__duracion
    def getTitulo(self):
        return self.__titulo