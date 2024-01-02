#!/usr/bin/env python3

class Animal:
    
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False

    def alimentar(self):
        self.alimentado = True

    def vender(self):
        self.alimentado = False

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - {'Alimentedo' if self.alimentado else 'Hambriento'}"

class TiendaAnimales:

    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)

    def alimentar_animales(self):
        for animal in self.animales:
            animal.alimentar()

    def vender_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                animal.vender()
                self.animales.remove(animal)
                return
                #break

        print(f"\nNo hay animales con este nombre en la tienda {nombre}")
                

if __name__ == '__main__':

    tienda = TiendaAnimales("ImpexAnimals")

    gato = Animal("Tijuana", "Gato")
    perro = Animal("Chop", "Perro")

    tienda.agregar_animal(gato)
    tienda.agregar_animal(perro)

    tienda.mostrar_animales()

    tienda.alimentar_animales()
    print(f"\t\n[+]Mostrando los animales despues de alimentarlos\n")
    tienda.mostrar_animales()

    tienda.vender_animal("Tijuana")
    print(f"Mostrando los animales una vez Tijuana se haya ido: \n")

    tienda.mostrar_animales()
    
