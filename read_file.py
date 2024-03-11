


try:

   with open("/Users/user/Documents/test.txt") as file :

    print(file.read())

    print(file.close())

except FileNotFoundError :
   print("sorry file not found !!!!!!")
