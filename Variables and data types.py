Types of dates
my_address = "192.168.1.9" -> String
port = 80 -> int
number = 4.5 -> float
number = str(4),int(4),float(4),int(4.1) -> type casting 
Lists:

#!/usr/bin/end python3

my_ports = []
my_ports.append(22)
my_ports.append(80)
my_ports.append(443)

for port in my_ports:

1.2
    print(f"Puerto: {port}")

1.3
  print(f"Puerto: " + str(port))

1.4 Represent all hoe many elements have the list
for port in my_ports:
    print(f"Puerto: {port}")

print(f"The lists have of {len(my_ports)} elements")

1.5 Do more simply the lists (Contemplate repetitions)
my_ports = [22, 80, 445, 8080, 445, 88]

for port in my_ports:
    print(f"Puerto: {port}")
print(f"The lists have of {len(my_ports)} elements")

1.6 With append you can add just an number, but with extend you can add what numbers or data do you want:
my_ports.extend([23, 21])
or
my_ports += [86, 87] = my_ports = my_ports + [86, 87]

ort The list
my_ports = sorted(my_ports)
delete elements
del my_ports[0] first element
delete elements 
```
del my_ports[0] first element
```
Delete the last element:
```
[8, 2, 'Hola', 9, 3, 4]
>>> mi_lista.pop()
4
```
insert elements
```
>>> mi_lista.insert(2, 9) -> in the second position insert the number 9
>>> mi_lista
[8, 2, 9, 3, 4]
```

1.7 
Find the index of the list
```
>>> mi_lista = [1, 3, 5, 6, 8, 10, 13, 14, 16, 18, 19, 21]
>>> mi_lista
[1, 3, 5, 6, 8, 10, 13, 14, 16, 18, 19, 21]
>>> mi_lista.index(14)
7
>>> 
```

Search an element, with .index -> Only show you de first element that you find
```
>>> mi_lista += [12]
>>> mi_lista += [1]
>>> mi_lista += [3]
>>> mi_lista.index(1)
0
>>> mi_lista
[1, 3, 5, 6, 8, 10, 13, 14, 16, 18, 19, 21, 12, 1, 3]
>>> mi_lista.index(1) 
0
>>> 
```

Enumerate the index and the element at the same time (x) is the index and (y) is the element
```
>>> for x, y in enumerate(mi_lista)
...     print(f"{x}: {y}")
... 
0: 1
1: 3
2: 5
3: 6
4: 8
5: 10
6: 13
7: 14
8: 16
9: 18
10: 19
11: 21
```

Filter for search an element conditionate by a index
```
>>> indices = [x for x, y in enumerate (mi_lista) if y == 14]
>>> indices
[7]
```

How many times an element is repeated
```
>>> mi_lista.count(14)
1
```

Remove repetitions with set
```
>>> mi_lista = [1, 5, 6, 7, 8, 9 ,7 , 7]
>>> mi_lista
[1, 5, 6, 7, 8, 9, 7, 7]
>>> set(mi_lista)
{1, 5, 6, 7, 8, 9}
>>> mi_lista = list(set(mi_lista))
>>> mi_lista
[1, 5, 6, 7, 8, 9]
>>> 
```

The max/min number 
```
>>> mi_lista
[1, 5, 6, 7, 8, 9]
>>> print(f"[+] The max number is {max(mi_lista)}") or min
[+] The max number is 9
>>> 
```

The average/sum/minus
```
>>> sum(mi_lista)
36
```

Average
```
>>> sum(mi_lista)
36
>>> len(mi_lista)
6
>>> sum(mi_lista) / len(mi_lista)
6.0
```

Total numbers
```
>>> sum(mi_lista)
36
>>> len(mi_lista)
6
>>> sum(mi_lista) / len(mi_lista)
6.0
```
Round
```
>>> round(sum(mi_lista) / len(mi_lista), 2)
5.27

