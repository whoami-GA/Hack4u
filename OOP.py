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

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property # con property haces como que el def es una propiedad  del objeto y no hace falta poner () en la llamada print
    def area(self): # Rectangulo.area(rect1)
        
        return self.ancho * self.alto
        
    def __str__(self):
        
        return f"\n[+] Propriedades del rectangulo: [Ancho: {self.ancho}] [Alto {self.alto}]"

    def __eq__(self, rect2):
                # slef.ancho(rect1) == self.ancho(rect2) and self.alto(rect1) == self.alto(rect2)
        return self.ancho == rect2.ancho and self.alto == rect2.alto



rect1 = Rectangulo(20, 80)
rect2 = Rectangulo(20, 80)
print(rect1)
print(f"\n[+] El area es {rect1.area}")
print(f"\n[+] Son iguales? -> {rect1 == rect2}")
print(f"\n-------\n")



class Libro:
rect1 = Rectangulo(20, 80)
rect2 = Rectangulo(20, 80)
print(rect1)
print(f"\n[+] El area es {rect1.area}")
print(f"\n[+] Son iguales? -> {rect1 == rect2}")
print(f"\n-------\n")



class Libro:

    IVA = 0.21
rect1 = Rectangulo(20, 80)
rect2 = Rectangulo(20, 80)
print(rect1)
print(f"\n[+] El area es {rect1.area}")
print(f"\n[+] Son iguales? -> {rect1 == rect2}")
rect1 = Rectangulo(20, 80)
rect2 = Rectangulo(20, 80)
print(rect1)
print(f"\n[+] El area es {rect1.area}")
print(f"\n[+] Son iguales? -> {rect1 == rect2}")
print(f"\n-------\n")



class Libro:

    IVA = 0.21
print(f"\n[+] Son iguales? -> {rect1 == rect2}")
print(f"\n-------\n")



class Libro:

    IVA = 0.21

    def __init__(self, titulo, autor, precio):

        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    @staticmethod # Decoradores, los cuales como argumentos no necesita el objeto como tal para operar sino que opera con los argumentos
    def es_bestseller(total_ventas): # Libro.es_bestseller(mi_libro, total_ventas)

        return total_ventas > 8000 

    @classmethod #Decoradores 
    def precio_con_iva(cls, precio):

        return precio + precio * cls.IVA

class LibroDigital(Libro):
    
    IVA = 0.10


mi_libro = Libro("Ai 25 de Lei?", "Adrian", 13.5)
mi_libro_digital = LibroDigital("Ai 15 lei pe card?", "Adrian", 13.5)
# Esto que le estamos pasando no es un atributo del objeto, no existe en el objeto
print(Libro.es_bestseller(9000))
print(f"\n[+]El precio del libro con IVA incluido es de {Libro.precio_con_iva(mi_libro.precio)}")
print(f"\n[+]El precio del libro digital con IVA incluido es de {LibroDigital.precio_con_iva(mi_libro_digital.precio)}")

