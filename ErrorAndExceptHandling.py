from pwn import log

try:

        num = 6/2

except ZeroDivisionError:

        log.failure("Is not divisible by zero")
    

except TypeError:
    
        log.failure("This not divisible")

else: 
    
        log.failure(f"The result of division is {num}")

finally:

        print("This always will execute")


x = -5

if x < 0:
        raise Exception("!No se puede utilizar Numero negativos") # raise sirve para lanzar exepcionces

try:
    int("Hello")
except:
    print("This not have any sens")
