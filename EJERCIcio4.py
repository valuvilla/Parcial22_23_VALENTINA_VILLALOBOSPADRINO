# Crear clase alumno con atributos de nombre y nota
# Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
# Crear un método llamado calificación que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota
# 


import unittest


class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumno creado con éxito")

    def __str__(self):
        return f"Alumno: {self.nombre} - Nota: {self.nota}"

    def calificacion(self,nota, nombre):
        if self.nota >= 5:
            print(f"El alumno {nombre} ha aprobado con {nota}")
        else:
            print(f"El alumno {nombre} ha suspendido {nota}")

class TestAlumno(unittest.TestCase):
    def test_calificacion(self):
        alumno1 = Alumno("Juan", 6)
        print(alumno1.__str__())
        alumno2 = Alumno("Ana", 4)
        print(alumno2.__str__())
        alumno3 = Alumno("Pedro", 7)
        print(alumno3.__str__())
        alumno2= Alumno("Maria", 3)
        print(alumno2.__str__())
    
if __name__ == "__main__":
    alumno1 = Alumno("Juan", 6)
    print(alumno1.__str__())
    alumno2 = Alumno("Ana", 4)
    print(alumno2.__str__())
    alumno3 = Alumno("Pedro", 7)
    print(alumno3.__str__())
    alumno2= Alumno("Maria", 3)
    print(alumno2.__str__())
    unittest.main()