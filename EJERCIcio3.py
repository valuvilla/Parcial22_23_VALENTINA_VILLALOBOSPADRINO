# Crear clase alumno con atributos de nombre y nota
# Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
# Crear un método llamado calificación que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota

import unittest


class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumno creado con éxito")

    def calificacion(self,nota, nombre):
        if self.nota >= 5:
            print(f"El alumno {nombre} ha aprobado con {nota}")
        else:
            print(f"El alumno {nombre} ha suspendido {nota}")
    
if __name__ == "__main__":
    alumno1 = Alumno("Juan", 6)
    alumno1.calificacion(alumno1.nota, alumno1.nombre)
    alumno2 = Alumno("Ana", 4)
    alumno2.calificacion(alumno2.nota, alumno2.nombre)
    alumno3 = Alumno("Pedro", 7)
    alumno3.calificacion(alumno3.nota, alumno3.nombre)
    alumno2= Alumno("Maria", 3)
    alumno2.calificacion(alumno2.nota, alumno2.nombre)