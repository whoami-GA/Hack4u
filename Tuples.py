#!/usr/bin/env python3

example = [1, "Test", 3, [1, 2 ,3], {'Shadow': 1 ,'Striker': 2 ,'Intruder': 3 ,'Dragstar': 4}, True]
example = (1, "Test", 3, (1, 2 ,3), {'Shadow': 1 ,'Striker': 2 ,'Intruder': 3 ,'Dragstar': 4}, True) # Inmutable, insert(), extend(), remove(), pop(), append(), do not work

print(example[1:3])
example[0] = 8 # Can no execute
print(example)

for element in example:
    print(element)

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
my_tuple_1 = (5, 6, 7, 8, 9)
my_tuple_2 = my_tuple + my_tuple_1
my_tuple_3 = my_tuple*3 
odd_numbers = tuple(i for i in my_tuple if i % 2 == 0)
even_numbers = tuple(i for i in my_tuple if i % 2 == 1)



a, b ,c ,d = my_tuple

print(a)
print(b)
print(c)
print(d)
print(f"This is the len on my tuple: " + str(len(my_tuple)) + "\n")
print(f"This is the len on my_tuple_2: " + str(len(my_tuple_2)) + "\n")
print(f"The result of multiply my_tuple * 3 and will repeat thil tuple 3 times: {my_tuple_3}")
print(odd_numbers)
print(even_numbers)

db1_credential = ("adrian", "////Pass")
db2_credential = ("Hackermate", "Hackermate1234")

try:
    db1_credential[0] = "Manolo"
except TypeError:
    print("You cand do that You can manipulate a tuple")
