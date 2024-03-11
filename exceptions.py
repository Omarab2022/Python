

try :

    x = int(input("enter number to devide"))
    y = int(input("enter number to devide by"))

    div = x / y



except ZeroDivisionError :
    print("you can t devide by zero")

except ValueError :
    print("you cant devide by string")
else:
    print(div)
finally:
    print("finnaly always run")
