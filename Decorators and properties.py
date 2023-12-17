#!/usr/bin/env python3

def mi_decorador(funcion): #funcion de orden superior , # llamar a una funcion antes de la funcion
    def envoltura():
        print("Estoy saludando en la envoltura de decorador antes de llamar al a funcion")
        funcion() # Llamada a la funcion original
        print("Estoy saludando en la envoltura del decorador despues de llamar a la funcion")
    return envoltura

@mi_decorador
def saludo():

    print("Hola estoy saludando dentro de la funcion")

saludo()
# --------
def ins(funcion):
    def envoltura():
        print("Antes de la funcion")
        funcion()
        print("Despues de la funcion")
    return envoltura

@ins # tiene que ser lo mismo como se llama el def
def insignias():
    print("1" ,"2", "3")

insignias()

print(f"-------------\n")

#@property # Getters y Setters

class Persona:

    def __init__(self, nombre, edad):

        self._nombre = nombre
        self._edad = edad

    @property 
    def edad(self): #Getter
        return self._edad

    @edad.setter #Setter # Cuando tu defines un propriedad para tu configurar el codigo es poner el proprio metodo y le metes setter
    def edad(self, valor): # hay que recivir un valor, asi que ponemos una variable, en este caso un valor
        if valor > 0:
            self._edad = valor
        else:
            raise ValueError("[!] Nu poti nu naste\n")

manolo = Persona("Manolo", 23)
manolo.edad = 4 # Setter
print(manolo.edad) #Getter
print(f"\n")
# ------------

class Data:

    def __init__(self, model, motor):
        
        self._model = model
        self._motor = motor
    
    @property
    def motor(self): # Getter
        return self._motor

    @motor.setter
    def motor(self, cilidrada): #cilidrara viene del motor
        if cilidrada > 1400:
            self._motor = cilidrada
            print("Vale, el coche va a salir a fabrica")    
        else:
            raise ValueError("Esto no es legal")
            
                

meta = Data("Insignia", 10000)
meta.motor = 54542 # Setter, con esto seteas
print(meta.motor) # Getter, con esto recives

print(f"--------------\n")

import time 

def cronometro(funcion): # Si el decoradoes eta puesto en las dos funciones estas pasan en la funcion de orden superior
    def envoltura(n): # n es num de las def
        inicio = time.time() # defino el tiempo
        funcion(n) # llamo a la funcion
        final = time.time() # para el contador para ver cuanto ha tardado
        
        print(f"Tiempo total transcurido en la funcion {funcion.__name__}: {final - inicio}")
    return envoltura

@cronometro
def pausa_corta(num):
    time.sleep(num)
             
@cronometro
def pausa_larga(num):
    time.sleep(num)

pausa_corta(0.3)
pausa_larga(0.2)

#----------
print(f"-----------\n")

# *args 
# estos argumentos tiene como output tuplas, argumentos posicionales 

def suma(*args):
    return sum(args)


print(suma(2, 3, 4, 14, 16, 12, 56))

print(f"-------------\n")

# **kwargs 
# Recive argumentos de clave valor

def presentacion(**kwargs):
    
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

presentacion(nombre="Marcelo", edad=65, ciudad="Tenerife", profesion="Lammer")

print(f"---------------\n")


import time 

def cronometro(funcion):
    def envoltura(*args, **kwargs): 
        inicio = time.time() 
        funcion() 
        final = time.time() 

        print(f"Tiempo total transcurido en la funcion {funcion.__name__}: {final - inicio}")

        if args:
            print(args)
        if kwargs:
            print(kwargs)
            print(f"= = = ")

        if 'nombre' in kwargs:
            print(kwargs['nombre'])
            print(args)
        else:
            print("No hay Dick")
    return envoltura

@cronometro
def pausa_corta(*args, **kwargs): # Recivas lo que recivas, interpretalo
    time.sleep(0.2)

@cronometro
def pausa_larga(): # Recivas lo que recivas, interpretalo
    time.sleep(0.2)

pausa_corta(2, 3, 4, 5, 6, 7,nombre="Batman", edad= 123)
pausa_larga()


print(f"-----------\n")


class Circumferencia:

    def __init__(self, radio):
        self._radio = radio

    @property # Getter
    def radio(self):
        return self._radio

    @property
    def diametro(self):
        return 2 * self._radio

    @property
    def area(self):
        return 3,1415 * (self._radio **2)


    @radio.setter # Setter
    def radio(self, valor):
        self._radio = valor

c = Circumferencia(5)

print(c.radio)
print(c.diametro)
print(c.area)
print(f"\n")

c.radio = 10
print(c.radio)
print(c.diametro)
print(c.area)
print(f"= = =\n")
#--------------

class Suma:

    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    @property
    def del_1(self):
        return self._num1
    
    @property
    def cuadrado(self):
        return self._num1 **2
    
    @property
    def hay(self):
        return f"La suma de los dos es: {self._num1 + self._num2}"

    @cuadrado.setter
    def cuadrado(self, value):
        self._num1 = value
    
    
numero = Suma(15, 24)
print(numero.del_1)
print(numero.cuadrado)
print(numero.hay)

numero.cuadrado = 10
print(numero.del_1)
print(numero.cuadrado)
print(numero.hay)
