from claseCarrera import Carrera as carrera

class Facultad:
    def __init__(self,cod,nom,dire,loc,tel):
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = dire
        self.__localidad = loc
        self.__telefono = tel
        self.__carreras = []

    def __str__(self):
        return '\nCodigo: %s Nombre: %s Direccion: %s Localidad: %s Telefono: %s' % (self.__codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono)



    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre

    def agregaCarrera(self,objeto):
        if(type(objeto) == carrera):
            self.__carreras.append(objeto)
        else:
            print('\nError, no se pudo cargar carrera.')



    def mostrar(self):
        for carrera in self.__carreras:
            print('\t',carrera)

    def buscarCarrera(self,nombre):
        for carrera in self.__carreras:
            if(carrera.getNombre() == nombre):
                dato = carrera.getCodigo()
                dato,dato2 = dato.split('.')
                return dato

    def borrar(self):
        for carrera in self.__carreras:
            print(carrera)
            del carrera
            print('------elimina ')