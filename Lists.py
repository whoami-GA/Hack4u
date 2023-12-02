#!/usr/bin/env python3

ports_tcp = [22, 21, 25, 80, 443, 8080, 88, 445, 69]
ports_tcp.append(5985) # Add To the list


for port in ports_tcp:
   print(f"This is the port {port}")

ports_tcp = [22, 21, 25, 80, 443, 8080, 88, 445, 69]
ports_tcp.append(5985)

ports_tcp.sort() #Sort The tcp list
print(ports_tcp)


attacks = ['Phising', 'DDos', 'SQL Injection', 'Man In The Middle', 'Cross-Site Scripting']
another_attacks_list = attacks[2:-2]
i = 0   #cont
attacks_uppercase = [attack.upper() for attack in attacks]
print(attacks_uppercase)


first_attack = attacks[2] # Acces to the first element of the list
print(another_attacks_list)

while i < len(attacks):
    print(attacks[i])
    i += 1
#for i, attack in enumerate(attacks): # enumerate returns an index and a value of this index from the item list
    print(f"For the position {i+1} we have the attack {attack}")


    # Reverse the lsit
attacks.reverse()
print(attacks)


cve_list = ['CVE-2023-1435', 'CVE-2022-2764', 'CVE-2015-5676', 'CVE-2010-4642']
cve_list.remove('CVE-2022-2764') # Remove an object from the list

print(cve_list)


    #combine Lists

names = ["Adrian", "Vasile", "Capraru", "15 lei", "Shadow", "Yamaha", "Honda", "Yapanese", "Yasou"]
ages = [23, 13, 15, 1998, 2007, 1945, 29, 67, 12]

for name, age in zip(names, ages): # zip applies a combinatorics to combine 2 or more fields
    print(f"{name} have {age} old")

del names[1] # to remove elements
print(names)

names.remove("Shadow")
print(names)

names.clear()
print(names)

delete_user = names.pop(0) # pot a deleted user in a variable
print(names)
print(delete_user)

 Alter the value of the elements and instert a new element

names.insert(2, "Chema Alonso") # Insert

names[2] = "Chema Alonso" # Reemplazar
    

    Extend the list
names.extend(ages)
print(names)
