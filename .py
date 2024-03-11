name = "omar abarra"
new_name = ""

for char in name:
    if char.islower():
        new_name += char.capitalize()
    else:
        new_name += char

print(new_name)
