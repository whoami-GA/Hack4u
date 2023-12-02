mi_set = {1, 2, 3, 4, 5, 6}
my_set_1 = {2, 4, 1, 9, 8}

finally_set = mi_set.union(my_set_1)

mi_set.add(4)
mi_set.update({4, 5, 6})
#mi_set.remove(7)
mi_set.discard(7)
mi_set.discard(4)

print(finally_set)


    #Verify a subSet
first_set = {1, 2, 3, 9}
second_set = {1, 2, 3, 4, 5}

print(first_set.issubset(second_set)) # Return a boolean status!!

    #Sort a list and convert a set in a list
set_1 = {"Hackermante", "S4vitar"}
set_2 = {"Hackermante", "S4vitar", "Lobotec"}

print(set_1.issubset(set_2))


my_list = [1, 5, 4, 6, 5, 1, 2, 2, 2 , 8, 1, 14, 12, 1, 1]

no_repeat = list(set(my_list))
print(no_repeat)
print(f"-------\n")



    #Efficently search
set_1_1 = set(range(10000))

print(1234 in set_1_1)
print(f"-----\n")


facebook_users = {"Shadow", "Striker", "Intruder", "Rebel"}
x_users = {"Shadow", "Striker", "Intruder", "M800", "Cargo"}

both_platforms = facebook_users.intersection(x_users)
all_users = facebook_users.union(x_users)

print(all_users)
print(both_platforms)


    #Difference!

platform_differences = facebook_users.difference(x_users)
print(platform_differences)
