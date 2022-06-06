from claseLista import Lista
from claseDecodificador import objectEncoder
from claseTelevisor import Televisor
from claseHeladera import Heladera
from claseLavarropa import Lavarropa

def menu():
    opcion = 0
    salir = False
    while not salir:
        print('\n-----------------MENU DE OPCIONES-------------')
        print('\n1-Insertar un aparato en una posicion determinada.')
        print('\n2-Agregar un aparato.')
        print('\n3-Mostrar Aparato en una posicion dada.')
        print('\n4-Mostrar la cantidad de T,H,L que son marca Philips.')
        print('\n5-Mostrar la marca de todos los lavarropas que tienen carga superior.')
        print('\n6-Mostrar para todos los aparatos, marca, pais e importe de venta.')
        print('\n7-Almacear los objetos en el archivo aparatoselectronicos.json')
        print('\n8-Salir.')
        opcion = int(input('\nIngrese opcion: '))

        if opcion == 1:
            posicion = input('\nIngrese nro de posicion: ')
            try:
                posicion = int(posicion)
                aparato = input('\nIngrese tipo de aparato(televisor(t),heladera(h),lavarropa(l)): ')
                marca = input('\nIngrese marca: ')
                modelo = input('\nIngrese modelo: ')
                color = input('\nIngrese color: ')
                pais = input('\nIngrese pais: ')
                precio = input('\nIngrese precio: ')
                if aparato == 't':
                    tipo = input('\nIngrese tipo: ')
                    pulgadas = input('\nIngrese pulgadas: ')
                    definicion = input('\nIngrese definicion: ')
                    conexion = input('\nIngrese conexion(V-F): ')
                    ap = Televisor(marca,modelo,color,pais,precio,tipo,pulgadas,definicion,conexion)
                    aparatos.insertarElemento(posicion,ap)
                elif aparato == 'h':
                    capacidad = input('\nIngrese capacidad en litros: ')
                    freezer = input('\nIngrese(V-F): ')
                    ciclica = input('\nIngrese(V-F): ')
                    ap = Heladera(marca,modelo,color,pais,precio,capacidad,freezer,ciclica)
                    aparatos.insertarElemento(posicion, ap)
                else:
                    capLavado = input('\nIngrese capacidad: ')
                    velocidad = input('\nIngrese velocidad: ')
                    cantProgramas = input('\nIngrese cant de programas: ')
                    tipo = input('\nIngrese tipo de carga: ')
                    ap = Lavarropa(marca,modelo,color,pais,precio,capLavado,velocidad,cantProgramas,tipo)
                    aparatos.insertarElemento(posicion, ap)

            except ValueError:
                print('\nDebe ser un numero entero....:')

        if opcion == 2:
            aparato = input('\nIngrese tipo de aparato(televisor(t),heladera(h),lavarropa(l)): ')
            marca = input('\nIngrese marca: ')
            modelo = input('\nIngrese modelo: ')
            color = input('\nIngrese color: ')
            pais = input('\nIngrese pais: ')
            precio = input('\nIngrese precio: ')
            if aparato == 't':
                tipo = input('\nIngrese tipo: ')
                pulgadas = input('\nIngrese pulgadas: ')
                definicion = input('\nIngrese definicion: ')
                conexion = input('\nIngrese conexion(V-F): ')
                ap = Televisor(marca, modelo, color, pais, precio, tipo, pulgadas, definicion, conexion)
                aparatos.agregar(aparato)
            elif aparato == 'h':
                capacidad = input('\nIngrese capacidad en litros: ')
                freezer = input('\nIngrese(V-F): ')
                ciclica = input('\nIngrese(V-F): ')
                ap = Heladera(marca, modelo, color, pais, precio, capacidad, freezer, ciclica)
                aparatos.agregar(aparato)
            else:
                capLavado = input('\nIngrese capacidad: ')
                velocidad = input('\nIngrese velocidad: ')
                cantProgramas = input('\nIngrese cant de programas: ')
                tipo = input('\nIngrese tipo de carga: ')
                ap = Lavarropa(marca, modelo, color, pais, precio, capLavado, velocidad, cantProgramas, tipo)
                aparatos.agregar(aparato)

        if opcion == 3:
            posicion = input('\nIngrese posicion: ')
            try:
                posicion = int(posicion)
                aparatos.buscaXPosicion(posicion)
            except ValueError:
                print('\nTiene que ser numero entero....')

        if opcion == 4:
            marca = 'philips'
            aparatos.buscaMarca(marca)

        if opcion == 5:
            carga = 'superior'
            aparatos.buscaCarga(carga)

        if opcion == 6:
            aparatos.importe()

        if opcion == 7:
            nuevo = aparatos.toJson()
            Json.guardarJSONArchivo(nuevo,'aparatoselectronicos.json')
            print('\nARCHIVO GUARDADO.')

        if opcion == 8:
            salir = True

        if opcion == 9:
            aparatos.mostrar()




if __name__ == '__main__':
    aparatos = Lista()
    Json = objectEncoder()
    Diccionario = Json.leerJSONArchivo('aparatoselectronicos.json')
    aparatos = Json.decodificarDiccionario(Diccionario)
    menu()
