#!/usr/bin/env python3

class Persona:
    #Methods are funciton are funcitons of the class 
    #Esto es un constructor              #Reciviendo los valores de nombre y edad como argumentos
    def __init__(self, nombre, edad):   # Persona.__init__(marcel, nombre, edad)
    #Aplicar la declaratoria para el objeto
        self.nombre = nombre
        self.edad = edad #self hace referencia al objeto que tu le estas pasando
    
    def saludo(self):   #Persona.saludo(marcelo)

        return f"Hola soy {self.nombre} y tengo tantos {self.edad} anos"

class Lidl:

    def __init__(self, lista):

        self.lista = lista

    def carro(self):
        
        return f"La lista es: {self.lista}"


compras = Lidl("Huevos") 
marcel = Persona("Marcel", 27)
juan = Persona("juan", 21)
compras = Lidl("Huevos")
print(juan.saludo())
print(marcel.saludo())
print(compras.carro())
print(f"\n-------\n")

#----------


class Animal:
    
    def __init__(self, nombre, animal): # Animal.__init__(gato, nombre, animal)

        self.nombre = nombre
        self.animal = animal

    def descripcion(self): #Anima.descripcion(obj)
        
        return f"{self.nombre} es un {self.animal}"
        print(f"{self.nombre} es un {self.animal}")

gato = Animal("Tijuana", "Gato")
perro = Animal("Chop", "Perro")


print(gato.descripcion()) # Esto va si print
print(perro.descripcion())
gato.descripcion() # Esto va print
perro.descripcion()
print(f"\n------\n")


class cuentaBancaria:
     #Se puede inicializar un atributo del constructor poniendo por ejemplo dinero = 0 
    def __init__(self, cuenta, nombre, dinero=0):
        self.cuenta = cuenta
        self.nombre = nombre
        self.dinero = dinero
    
    # Donde ponga self.dinero es el objeto, donde ponga  es el dinerp de la clase
    def depositar_dinero(self, dinero): # CuentaBancaria.depositar_dinero(manolo)
        self.dinero += dinero
        return f"\n[ [{self.nombre}] Se han depositado {dinero} euros, el balance de la cuenta es {self.dinero} euros]"
    
    def retirar_dinero(self, dinero):
        
        if dinero > self.dinero:
            return f"\n[!] [{self.nombre}] Fondos insuficientes\n"
        
        self.dinero -= dinero # self.dinero = self.dinero - dinero

        return f"\n[ [{self.nombre}] Se han retirado {dinero} euros, el balance de la cuenta es {self.dinero} euros]"


manolo = cuentaBancaria("213412FDSFG324532", "Sancho Panza", 1000)
marcelo = cuentaBancaria("213412sdffsdSDFG", "Marcelo Sub", 13)


print(manolo.depositar_dinero(500))
print(manolo.retirar_dinero(935))
print(manolo.retirar_dinero(1000))


print(marcelo.retirar_dinero(5))
print(f"\n-------\n")


class Rectangulo:

