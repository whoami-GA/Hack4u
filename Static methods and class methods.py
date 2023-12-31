#!/usr/bin/env python3


class Calculadora:


    @staticmethod # staticmethod do not oper with objects
    def suma(num1, num2):
        
        return num1 + num2

    @staticmethod
    def resta(num1, num2):

        return num1 - num2

    @staticmethod
    def multiplicacion(num1, num2):

        return num1 * num2

    @staticmethod
    def division(num1, num2):

        return num1 / num2 if num2 !=0 else "\n Dramatic Error Do Not Divided By 0"

print(Calculadora.suma(2, 8))
print(Calculadora.resta(8, 4))
print(Calculadora.multiplicacion(8, 8))
print(Calculadora.division(8, 8))

#----

class Automovil:
    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo

    @classmethod
    def  deportivos(cls, marca):
        
        return cls(marca, "deportivo")

    @classmethod
    def sean(cls, marca):

        return cls(marca, "Sean")

    def __str__(self): # necesita un self

        return f"La marca {self.marca} se un modelo {self.modelo}"

deportivo = print(Automovil.deportivos("Ferrari")) # Automovil("Ferrari", "Deportivo")
sean = print(Automovil.sean("Toyota")) # Automovil("Toyota", "Sean")



class Estudiantes:

    estudiantes = []

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
        Estudiantes.estudiantes.append(self)

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18

    @classmethod
    def crear_estudiante(cls, nombre, edad):
        if cls.es_mayor_de_edad(edad):
            return cls(nombre, edad)
        else:
            print(f"\t[+]El usuario {nombre} es menor de edad")

    @staticmethod
    def monstrat_estudiantes():
        for i, estudiante in enumerate(Estudiantes.estudiantes):
            print(f"[+]Estudiante numero [{i+1}]: {estudiante.nombre}")

Estudiantes.crear_estudiante("Hackermate", 43)
Estudiantes.crear_estudiante("Adrian", 32)
Estudiantes.crear_estudiante("Xeroxec", 12)
Estudiantes.crear_estudiante("Hackavis", 8)
Estudiantes.crear_estudiante("LoboTec", 98)


print(f"\n [i] Existent Students \n")

Estudiantes.monstrat_estudiantes()

