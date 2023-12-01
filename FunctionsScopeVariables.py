def saludo(name): # Here you are waiting for a signal whos comes from the call of function
    print(f"\nHello {name}")

saludo("Manuel")

def sum(x, y):
    return x + y # When do you whant to a return of function

result = sum(2, 8)

print(f"\n[]The Sum from the two value is {sum(9 ,3)}")


    #Scope of The Valiables

global_var = "I am Global"
local_variable = "I am The out variable"

def function():
     local_variable = "I am Local" # only exist into  the function, out it is not recognized
     print(local_variable)
    print(global_var)


function()

print(global_var)
print(local_variable)


variable = "I am The out variable"
var = "I am a simple var"


def function():
    global variable
    global var
    variable = "I am Local and am i was changed" # only exist into  the function, out it is not recognize
    var = "I am the new simple var but I am in"
    print(variable)
    print(var)


function()

print(var)
print(variable)
