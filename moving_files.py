import os

source ="/Users/user/Documents/iti.txt"

destination = "/Users/user/Desktop/test.txt"


try:

    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source,destination)
        print(source + " is moved to " + destination)

except FileNotFoundError :
    print(" file not found")

