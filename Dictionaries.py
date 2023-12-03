#!/usr/bin/env python3

my_dictionary = {"name": "Adrian", "age": 27, "country": "Germany"}
    
    #Alter the dictionary
my_dictionary["name"] = "Changed"

    # Add new objects
my_dictionary["Profesion"] = "lammer"

    #Find in the dictionary
print(my_dictionary.get("name", "No found"))
print(my_dictionary.get("names", "No found"))

    #Remove
del my_dictionary["age"]

print(f"\n-----\n")
print(my_dictionary)
print(my_dictionary["country"])
print(f"The lenght of the dictionary is {len(my_dictionary)}")

print(f"\n----\n")


if "country" in my_dictionary:
    print(f"This key exists in the dictionary")

for key, value in my_dictionary.items():
    print(f"For the key {key} we have the value {value}")


    #We can delete all the elements
#my_dictionary.clear()
print(my_dictionary)
print(f"\n-----\n")

#-----

    # Squares
squares = {x: x**2 for x in range(6)}

print(squares[5])

    # Print all the key and the valuess

print(squares.keys())
print(squares.values())
print(f"\n---\n")

    #Extend an diccionary

my_dictionary2 = {"motor": "honda", "dogs": "chop"}
my_dictionary.update(my_dictionary2)
print(my_dictionary)

    # Nested Dicctionary

my_dyct = {
    "name": "Adrian",
    "hobbies": {"primero": "music", "segundo": "creating"},
    "age": 27
}

print(f"\n----\n")
print(my_dyct["hobbies"]["segundo"])

    #Iterating 

the_list = {"nombre": "Adrian", "age":27, "country": "germany"}

for key, value in the_list.items():
    print(f"The [{key}] is [{value}]")
