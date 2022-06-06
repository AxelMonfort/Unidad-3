from claseDecodificador import objectEncoder
from claseLista import Lista
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocenteInvestigador import DocenteInvestigador
from claseApoyo import Apoyo
import json

def menu():
    opcion = 0
    salir = False
    while not salir:
        print('\n===============MENU DE OPCIONES=================')
        print('\n1-Insertar personal a la lista.')
        print('\n2-Aregar personal a la lista.')
        print('\n3-Dada una posicion, mostrar que personal se encuentra en esa posicion.')
        print('\n4-Ingresar una carrera y listar todos los Docentes-Investigadores.')
        print('\n5-Dada una area de investigacion, contar la cant de Docentes_Investigador y la cant de investigadores.')
        print('\n6-Generar un listado que muestre: NyA,tipo de personal y sueldo, ordenado alfabeticamente.')
        print('\n7-Dada una categoria(I,II,III),listar NyA e importe extra por docencia e investigacion.')
        print('\n8-Guardar los datos en personal.json')
        print('\n9-Salir.')
        opcion = int(input('\nIngrese opcion: '))

        if opcion == 1:
            pos = int(input('\nIngrese posicion: '))
            tipo = input('\nIngrese tipo de persona a insertar(D,A,I,DI): ')
            cuil = input('\nIngrese cuil: ')
            apellido = input('\nIngrese apellido: ')
            nombre = input('\nIngrese nombre: ')
            sueldo = input('\nIngrese sueldo: ')
            antiguedad = input('\nIngrese antiguedad: ')
            if tipo == 'D':
                clases = int(input('\nIngrese cant de clases: '))
                cargo = input('\nIngrese cargo: ')
                catedra = input('\nIngrese catedra: ')
                persona = Docente(cuil,apellido,nombre,sueldo,antiguedad,clases,cargo,catedra)
                personal.insertar(pos,persona)
            elif tipo == 'A':
                categoria = input('\nIngrese categoria(I,II,III): ')
                persona = Apoyo(cuil,apellido,nombre,sueldo,antiguedad,categoria)
                personal.insertar(pos,persona)
            elif tipo == 'I':
                area = input('\nIngrese area: ')
                tipo = input('\nIngrese tipo: ')
                persona = Investigador(cuil,apellido,nombre,sueldo,antiguedad,area,tipo)
                personal.insertar(pos,persona)
            elif tipo == 'DI':
                clases = int(input('\nIngrese cant de clases: '))
                cargo = input('\nIngrese cargo: ')
                catedra = input('\nIngrese catedra: ')
                area = input('\nIngrese area: ')
                tipo = input('\nIngrese tipo: ')
                categoriaD = input('\nIngrese categoria: ')
                importe = int(input('\nIngrese importe: '))
                persona = DocenteInvestigador(cuil,apellido,nombre,sueldo,antiguedad,area,tipo,clases,cargo,catedra,categoriaD,importe)
                personal.insertar(pos,persona)
            else:
                print('\nCaracter incorrecto.')

        if opcion == 2:
            tipo = input('\nIngrese tipo de persona a insertar(D,A,I,DI): ')
            cuil = input('\nIngrese cuil: ')
            apellido = input('\nIngrese apellido: ')
            nombre = input('\nIngrese nombre: ')
            sueldo = input('\nIngrese sueldo: ')
            antiguedad = input('\nIngrese antiguedad: ')
            if tipo == 'D':
                clases = int(input('\nIngrese cant de clases: '))
                cargo = input('\nIngrese cargo: ')
                catedra = input('\nIngrese catedra: ')
                persona = Docente(cuil, apellido, nombre, sueldo, antiguedad, clases, cargo, catedra)
                personal.agregarPersona(persona)
            elif tipo == 'A':
                categoria = input('\nIngrese categoria(I,II,III): ')
                persona = Apoyo(cuil, apellido, nombre, sueldo, antiguedad, categoria)
                personal.agregarPersona(persona)
            elif tipo == 'I':
                area = input('\nIngrese area: ')
                tipo = input('\nIngrese tipo: ')
                persona = Investigador(cuil, apellido, nombre, sueldo, antiguedad, area, tipo)
                personal.agregarPersona(persona)
            elif tipo == 'DI':
                clases = int(input('\nIngrese cant de clases: '))
                cargo = input('\nIngrese cargo: ')
                catedra = input('\nIngrese catedra: ')
                area = input('\nIngrese area: ')
                tipo = input('\nIngrese tipo: ')
                categoriaD = input('\nIngrese categoria: ')
                importe = int(input('\nIngrese importe: '))
                persona = DocenteInvestigador(cuil, apellido, nombre, sueldo, antiguedad, area, tipo, clases, cargo, catedra, categoriaD, importe)
                personal.agregarPersona(persona)
            else:
                print('\nCaracter incorrecto.')

        if opcion == 3:
            pos = input('\nIngrese posicion a mostrar: ')
            personal.buscaXPosicio(pos)

        if opcion == 4:
             carrera = input('\nIngrese nombre de carrera: ')
             personal.buscarNombre(carrera)

        if opcion == 5:
            area = input('\nIngrese area de investigacion: ')
            personal.buscarArea(area)

        if opcion == 6:
            personal.listadoApellidos()

        if opcion == 7:
            categoria = int(input("Ingrese la categoría que desea revisar el importe total (Del 1 al 5):  "))
            while categoria < 1 or categoria > 5:
                print("Error, intente de nuevo.")
                categoria = int(input("Ingrese la categoría que desea revisar el importe total (Del 1 al 5):  "))
            personal.muestraCategoria(categoria)

        if opcion == 8:
            nuevo = personal.toJson()
            json.guardarJSONArchivo(nuevo, 'aparatoselectronicos.json')
            print('\nARCHIVO GUARDADO.')

        if opcion == 9:
            salir = True



if __name__ == '__main__':
    personal = Lista()
    json = objectEncoder()
    dic = json.leerJSONArchivo("personal.json")
    json.decodificarDiccionario(dic)
    menu()
