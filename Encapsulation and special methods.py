#!/usr/bin/env python3

#class Ejemplo:
#    def __init__(self):

        #Atributo protegido 
        #self._atributo_protegido = "Soy un atributo protegido"

        #Atributo privado
#        self.__atributo_privado = "Soy un atributo privado y no deberias poder verme" # name mangling

#ejemplo = Ejemplo()
#print(ejemplo._atributo_protegido)
#print(ejemplo._atributo_privado)

#class Coche:
    
#    def __init__(self, marca, modelo):
#        self.marca = marca
#        self.modelo = modelo
#        self.__kilometraje = 0 # Privado

#    def conducir(self, kilometros):

#        if kilometros >=0:
#            self.__kilometraje += kilometros
#        else:
#            print("\n[!] Los kilometros deben ser mayores a 0\n")

#    def mostrar_kilometros(self):
        
#        return self.__kilometraje

#coche = Coche("Toyota", "Corolla")
#coche.conducir(150)
#print(coche.mostrar_kilometros())


class Libro:

    def __init__(self, autor, titulo):

        self.autor = autor
        self.titulo = titulo

    def __str__(self):

        return f" El libro {self.titulo} ha sido escrito por el autor {self.autor}"
    #Metodo de igualdad Devuelve un metodo buleano
    def __eq__(self, otro):

        return self.autor == otro.autor and self.titulo == otro.titulo

libro = Libro("Marcelo Vazquez", "Como ser Lammer?")
libro_2 = Libro("Pepito Gonzales", "Como ser Lammer?")

print(libro)
print(f"Son iguales ambos libros? -> {libro == libro_2}")

class Check:
    
    def __init__(self, force, presure):

        self.force = force
        self.presure = presure

    def __str__(self): #Combinacion de las exprimido en str

        return f"La fuerza es {self.force} y la presion es {self.presure}"

    def __eq__(self, other):
        
        return self.presure == other.presure
        # self.force == other.force, solo las fuerzas
        # return self.force == other.force and self.pressure == other.pressure, las dos a la Vazquez
        # self.pressure == other.pressure, las presiones


force = Check(21, 6325.4)
force2 = Check(32, 6325.4)
print(force)
print(f"Esto es gual? -> {force == force2}")


#-----------------------

class CuentaBancaria:
    
    def __init__(self, num_cuenta, titular, saldo_inicial=0):
        
        self.num_cuenta = num_cuenta
        self.titulo = titular
        self.__saldo = saldo_inicial # self.saldo inicial, es la que no se deberia referenciar en el codigo

    def depositar_dinero(self, cantidad):
    
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"\n[+] Saldo actual en la cuenta {self.__saldo}")
        else:
            print("\n[!] El monto a depositar es incorecto")

    def retirar_dinero(self, cantidad):

        if cantidad > 0:
            if cantidad > self.__saldo:
                print("f\n[!] No tienes suficientes fondos")
            else:
                self.__saldo -= cantidad
                print(f"\n[+] Saldo actual en la cuenta {self.__saldo}")
        else:
            print("\n[!] El monto a retirar es incorecto")

    def mostrar_dinero(self):
        
        return f"\n[+] El saldo actual en la cuenta es: {self.__saldo}\n"

manolo = CuentaBancaria("12342", "Vasile Capraru", 350.20)
manolo.depositar_dinero(500)
manolo.retirar_dinero(200)
print(manolo.mostrar_dinero())


#----------------


class Caja:

    def __init__(self, *items): # Representa una lista e puede iterar por ella representa tuplas o tuples

        self.items = items

    def mostrar_items(self):

        print(type(self.items))

    def __len__(self):

        return len(self.items)


caja = Caja("Manzana", "Platano", "kiwi", "Pera")
print(len(caja))
print(f"--------------\n")

class Flores:

    def __init__(self, *numeros):

        self.numeros = numeros

    def lista(self):
        return f"{self.numeros}"

flor = Flores("Maria", "Juana", "Jhona", "Thomsten")
print(flor.lista())

#--------------------

class Pizza:

    def __init__(self, size, *ingredientes):

        self.size = size
        self.ingredientes = ingredientes

    def descripcion(self):

        print(f"Esta pizza tiene {self.size} cm de longitud y los ingredientes son: {', '.join(self.ingredientes)}")

pizza = Pizza(12, "Chorizo", "Jamon", "Queso", "Bacon", "Cebolla")

pizza.descripcion()

class Piezas:
    
    def __init__(self, *piezas):

        self.piezas = piezas

    def lista(self):

        return f"Estas es la lista de piezas que necesitamos: {', '.join(self.piezas)}"

lista_piezas = Piezas("Neumaticos", "Aceite", "Motor", "Algoritmos")

print(lista_piezas.lista())


print(f"------------------\n")



class MiLista:

    def __init__(self):

        self.data = [1, 2, 3, 4, 5, 6]


    def __getitem__(self, index): # Retornar de la lista el valor que le des.

        return self.data[index]

lista = MiLista()
print(lista[2])
print(f"--------------------\n")


# --------------

class Saludo:

    def __init__(self, saludo):

        self.saludo = saludo 
    
    def __call__(self, nombre): # Call recibir como argumento de la funcion 

        return f"{self.saludo} {nombre}"

hola = Saludo("Hola")
print(hola("Luis"))
print(hola("Alberto"))
print(f"--------------\n")

# --------------------

class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):

        return Punto(self.x + otro.x, self.y + otro.y) # crear un instancia temporal 

    def __str__(self):

        return f"({self.x}, {self.y})"

p1 = Punto(2, 8)
p2 = Punto(4, 9)

print(p1 + p2) # (6, 17)


class Matematicas:
    
    def __init__(self, i, z):
        self.i = i
        self.z = z
    
    def __add__(self, otro):

        return Matematicas(self.i + otro.i, self.z + otro.z)
    
    def __str__(self):

        return f"({self.i}, {self.z})"

z1 = Matematicas(3, 7)
z2 = Matematicas(12, 13)
print(z1 + z2)


print(f"---------\n")


class Contador:

    def __init__(self, limite):

        self.limite = limite

    def __iter__(self):
        
        self.contador = 0

        return self
    
    def __next__(self):

        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        else:
            raise StopIteration    

c = Contador(15)

for i in c:
    print(i)

# __add__ __eq__ __sub__ __mul__ __lt__
