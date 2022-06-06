from claseColeccion import Coleccion
from claseNatural import Natural
from claseElectrico import Electrico

def menu(coleccion,natural,electrico):
    opcion = 0
    salir = False
    total,total1 = 0,0
    while not salir:
        print('\n==========MENU DE OPCIONES==============')
        print('\n1-Marca y modelo del calefactor a gas natural de menor costo de consumo.')
        print('\n2-Marca  y modelo del calefactor eléctrico de menor consumo.')
        print('\n3-Tipo de calefactor y todos los datos del calefactor de menor consumo.')
        print('\n4-Salir')
        opcion= int(input('\nIngrese opcion: '))

        if opcion == 1:
            costo = int(input('\nIngrese costo por m3: '))
            cant = int(input('\nCantidad que se va a consumir: '))
            total = cant/costo
            datos = coleccion.buscar()
            print('\nCalefactor a gas natural que menos consume.')
            print('\n    Marca: '+str(datos[0]),'  Modelo: '+str(datos[1]))
            print('\n    Total: ',total)

        if opcion == 2:
            costo = int(input('\nIngrese costo por kilowatt: '))
            cant = int(input('\nCantidad que se va a consumir por hora: '))
            total1 = cant / costo
            datos = coleccion.buscar2()
            print('\nCalefactor electrico que menos consume.')
            print('\n    Marca: ' + str(datos[0]), '  Modelo: ' + str(datos[1]))
            print('\n    Total: ', total1)

        if opcion == 3:
            if total < total1:
                datos = coleccion.buscar()
                print('\nCalefactor a gas natural que menos consume.')
                print('\n    Marca: ' + str(datos[0]), '  Modelo: ' + str(datos[1]))
                print('\n    Total: ', total)
            else:
                datos = coleccion.buscar2()
                print('\nCalefactor electrico que menos consume.')
                print('\n    Marca: ' + str(datos[0]), '  Modelo: ' + str(datos[1]))
                print('\n    Total: ', total1)

        if opcion == 4:
            salir = True

        if opcion == 5:
            print(coleccion)


if __name__ == '__main__':
    cant = int(input('\nIngrese cantidad de calefactores: '))
    objCole = Coleccion(cant)
    objNatural = Natural
    objElec = Electrico
    objCole.agregar()
    menu(objCole,objNatural,objElec)