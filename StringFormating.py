
name = "S4vitar"
rol = "Begginer"
age = 26

print("Hello, I have {},{}!".format(age,rol))

print("Hello, I am {}!".format(rol))

print(f"Hello, I am {name}!") # f strings

print("Hello, I am {1} I am {0}, and my name is {2}".format(age, rol, name)) # playing with index. 

print("My name is %s and I am am %s and my age is %d" % (name, rol, age)) # %s or %d work for numbers, %d comes from decimals

#Pactice

Planet = "Earth"
System = ["Mercury", "Venus", "Saturn", "Neptun"]

def sistem():
    for star in System:
        print(f"I leave in the {planet[0]}")
        print(f"I leave in the {Planet}")
        print("All the Othr Planets are %s" % (System[0]))
        print(star)
        time.sleep(1)
        print("I leave in %s but i have to go to %s" % (System[1],System[2]))

sistem()

print("I am planet {0[1]}".format(System, Planet)) # Planet System[0] and [1 is Venus]
