from claseDocente import Docente
from claseInvestigador import Investigador
from claseApoyo import Apoyo
from claseNodo import Nodo
from claseDocenteInvestigador import DocenteInvestigador
from claseInterfaz import Elemento
from zope.interface import implementer

@implementer(Elemento)
class Lista:
    __comienzo = None
    __indice = None
    __actual = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self.__indice += 1
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarPersona(self,persona):
        try:
            if (type(persona) == Docente) or (type(persona) == Apoyo) or (type(persona) == Investigador) or (type(persona) == DocenteInvestigador):
                nodo = Nodo(persona)
                if self.__comienzo == None:
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo = nodo
                    self.__actual = nodo
                    self.__tope += 1
                else:
                    aux = self.__comienzo
                    while aux.getSiguiente() != None:
                        aux = aux.getSiguiente()
                    nodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(nodo)
                    self.__tope += 1
                print('\n***PERSONA AGREGADA CON EXITO***')
        except TypeError:
            print('\n No es una persona.')

    def insertar(self,pos,persona):
        if pos<=self.__tope:
            nodo = Nodo(persona)
            if pos == self.__comienzo:
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo = nodo
                self.__tope += 1
            else:
                aux = self.__comienzo
                nro = 1
                while nro<pos:
                    aux = aux.getSiguiente()
                    nro +=1
                nodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nodo)
                self.__tope += 1
            print('\nPersona insertada correctamente.')

    def buscaXPosicio(self,pos):
        if pos == 0:
            print(self.__comienzo.getNombreClase())
        else:
            aux = self.__comienzo.getSiguiente()
            band = False
            nro = 1
            while aux != None and band == False:
                if nro == pos:
                    band = True
                else:
                    aux = aux.getSiguiente()
                    nro +=1
            if band == True:
                print(aux.getNombreClase())
            else:
                print('\nNingun personal se encuentra en esa posicion.')

    def buscarNombre(self,carrera):
        aux = self.__comienzo
        while aux != None:
            if aux.getNombreClase() == 'DocenteInvestigador':
                if aux.getDato().getCategoriaD() == carrera:
                    print(aux.getDatos())
            aux = aux.getSiguiente()

    def buscarArea(self,area):
        aux = self.__comienzo
        cont,cont1 = 0,0
        while aux != None:
            if aux.getNombreClase() == 'DocenteInvestigador':
                cont +=1
            if aux.getNombreClase() == 'Investigador':
                if aux.getDato().getArea() == area:
                    cont1 +=1
            aux = aux.getSiguiente()
        print('\nLa cant de investigadores en esa area es de ',cont1)
        print('\nLa cant de docentes-investigadores es de ',cont)

    def muestraAlfabeticamente(self, lista, long):  # Ordena alfabeticamente y muestra los datos del Personal. Inciso 6
        j = 0
        aux = self.__comienzo
        while aux is not None:
            personal = aux.getDato()
            compara = personal.getApellido()
            if compara == lista[j]:
                j += 1
                print("NOMBRE: {} - APELLIDO: {} - CUIL: {} - SUELDO: ${} - ANTIGÜEDAD: {} - TIPO: {}".format(
                    personal.getNombre().center(10), personal.getApellido().center(10), personal.getCuil(),
                    personal.getSueldo(), personal.getAntiguedad(), type(personal)))
                if j != long:
                    aux = aux.getSiguiente()
                    if aux is None:
                        aux = self.__comienzo
                else:
                    aux = None
            else:
                aux = aux.getSiguiente()
                if aux is None:
                    aux = self.__comienzo

    def listadoApellidos(self):  # Listado de apellidos. Inciso 6
        apellidos = []
        for i in self:
            apellido = i.getApellido()
            apellidos.append(apellido)
        apellidos.sort()
        self.muestraAlfabeticamente(apellidos, len(apellidos))

    def muestraCategoria(self, categoria):
        acum = 0
        for i in self:
            if type(i) == DocenteInvestigador:
                if i.getCategoriaInvestigacion() == categoria:
                    print("APELLIDO: {} - NOMBRE: {} - EXTRA: {}".format(i.getApellido().center(10),
                                                                         i.getNombre().center(20), i.getImporteExtra()))
                    acum += i.getImporteExtra()
        if acum == 0:
            print("No existen Docentes investigadores con la categoría ingresada.")
        else:
            print("La Secretaría de Investigación, debe solicitar al Ministerio un total de ${} de importe extra".format(acum))


    def toJson(self):
        aparatos = []
        for v in self:
            aparatos.append(v.toJson())
        dic = dict(__class__=self.__class__.__name__, datos=aparatos)
        return dic