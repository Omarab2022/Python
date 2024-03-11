import os


file= "/Users/user/Documents/delete.txt"

try:
    if os.path.exists(file):
        os.remove(file)
        print(file + " is removed successfully")

except FileNotFoundError :
    print("file not found")

    #rmdir => delete folder
    #rmtree => delete folder contain files