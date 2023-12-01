square = lambda x: x**2 
print(square(6))

print(square(6))


sum = lambda x, y: x + y
print(sum(5, 4))


my_list = [1, 2, 3, 4, 5]

squars = list(map(lambda x: x**2, my_list)) # Map it creat to us a function and at iterable #list a map function

print(squars)



order = [1, 2, 3, 4]
order1 = [2, 3, 5, 7]

def test(n):
    return n + n

result = map(test , order1)
print(list(result))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))


    #filer
my_list1 = [1, 2, 3, 4, 5]

odd = list(filter(lambda x: x % 2 != 0, my_list1))

print(odd)


from functools import reduce
    #From functtools #reduce
multy = [1, 2, 3, 4, 5]

result1 = reduce(lambda x, y: x * y, multy) #Reduce que hace es realizarte toda la operatoria para todos lo elementos
                                            #x, y = 1 y y = 2, # despues x = 2 e y = 3 entonces 2 * 3 = 6

print(result1)
