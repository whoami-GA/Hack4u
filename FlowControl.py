#Conditionals and Loops

    
    Itering lists
names = ["Mercur", "Venus", "Earth", "Mars", "Venus"]

for name in names:
        print(f"The name for this planets are: " + name)



names = ["Mercur", "Venus", "Earth", "Mars", "Venus"]

for name in names:
        print(f"The name for this planets are: {name}")


    #Enumerate lists
    
names = ["Mercur", "Venus", "Earth", "Mars", "Venus"]

for i, name in enumerate(names): #Enumerate Always Return the index and the value
    print(f"The zone is {i+1} and the planet are {name}")


    Itering Dictionaries, Have 2 objects, the the key and the value, the value are unique
fruits = {"Apple": 1, "Banana": 5, "Kiwi": 3}

for fruit, quiantity in fruits.items():
    print(f"There are {quiantity} {fruit}")



#   Nested Loops

mi_list = [[1,4,5], [2,3,8], [9, 4, 1]]

for element in mi_list:
    print(f"\n[+] We are in the list: {element}")
    for element_in_list in element:
        print(element_in_list)

#   Compresion list for

odd_list = [1, 3, 5, 7, 9]
square =[i ** 2 for i in odd_list]

print(square)


for i in range(10):
    
        print(i) #with 5
    
    if i == 5:
        break # Stop the iteration
        continue # The number 5 is not includet
        print("Currently 'i' is 5")
    else:
        print("Currently 'i' is not 5")
    print(i) # without 5



for i in range(6):
     
    if i == 10:
        break 

else:   # the loop have an else. but have to stay out of the loop
    print("The Loop is okey")

# ----------
print("The script is working")


i = 0 

while i < 16:
    if i == 10:
        print("We are Exiting")
        break

    i += 1

else:
    print("The loop is over")

# ------
print("We are Out of Loop")

    #Conditionals

Age = 12 

if Age < 18:
    print("You are Mayor")
else:
    print("You are Minor")

if Age < 13:
    print("You are a Baby")
elif 13 <= Age < 18:
    print("Adolescent")
else:
    print("You are a Adult!")

Age = 2

result = "You are Adult!" if Age >= 18 else "You are Minor"

print(result)

    #And # (!) this simbol represent the is not

Age = 20
Nationality = "romania"

if Age >= 18 and Nationality == "Romania":
    print("You can Vote!")
else:
    print("You can't vote!")

    #Or
if Age >= 18 or Nationality != "Romania":
      print("You can Vote")
else:
    print("You can't vote!")

    #Nested Conditional we have pass too

if Age >= 18:
    if Nationality == "romania":
        print("You can vote!")
        pass


mi_lista = [1, 4, 6, 12, 14, 18, 373]

if 18 in mi_lista:
    print("We found it")
else:
    print("18 is not in the list")

    #Divide in a  for loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number %2 == 0: # divide by 0 is odd divide by 1 there are the even numbers
    #if number == 5:
        continue
    print(number)

numbers = [2, 4, 6, 8, 10]
all_are_odd = True

for number in numbers:
    if number %2 !=0:
        all_are_odd = False
        break
if all_are_odd:
    print("Succes are Odd")
else:
    print("You have an even in the list")
