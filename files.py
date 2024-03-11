import os


path = "/Users/user/Documents/iti.txt"

if os.path.exists(path):
    print("file exists")
    if os.path.isfile(path):
        print("this is a file")
else:
    print("file does not exixst")