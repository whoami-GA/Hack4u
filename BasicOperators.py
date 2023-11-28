#!/usr/bin/end python3


    #Sum
first_number = 6
second_number = 12

result = first_number + second_number 

print(result)


    #Minus
first_number = 6
second_number = 12

result = first_number - second_number 

print(result)

     
     #Multiply
first_number = 6
second_number = 12

result = first_number * second_number 

print(result)

   

     #Divide
first_number = 6
second_number = 12

result = first_number / second_number 

print(result)

  
     #Powers 6^12
first_number = 6
second_number = 12

result = first_number ** second_number 

print(result)


     
     #Fromat
first_number = 6
second_number = 12

result = first_number ** second_number 

print("{:,}".format(result).replace(",", ".")) # with : you start the format specificacionts and , is using to separe the decimals

     
     #The rest of the division
first_number = 6
second_number = 12

result = first_number % second_number #6 / 12 = 6 the rest to 12 is 6

print(result)

     
     #Multiply
first_str = "Hola"
second_str = " "
third_str = "Beauty"

print(first_str + second_str + third_str)
print(first_str*3)
print(first_str[0:3]*3)

    # Sum lists
odd_elements = [1, 3, 5, 7, 9]
even_elements = [2, 4, 6, 8, 10]

result = list(map(sum ,zip(odd_elements, even_elements))) # map help you to sum, divide, Multiply the retult of touple elements
print(result) # list of the  map touple
 
for element in result:
    print(element)
