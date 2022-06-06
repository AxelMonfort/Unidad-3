from clasePersonal import Personal
from claseDocente import Docente
from claseInvestigador import Investigador
from claseApoyo import Apoyo
from claseLista import Lista
from claseDocenteInvestigador import DocenteInvestigador
from pathlib import Path
import json

class objectEncoder(object):
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'Lista':
                persona = d['personal']
                manejador = class_()
                for i in range(len(persona)):
                    dPersona = persona[i]
                    class_name = dPersona.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dPersona['__atributos__']
                    unaPersona = class_(**atributos)
                    manejador.agregarPersona(unaPersona)
                return manejador