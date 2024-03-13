


dictionnary ={'new york':"snowing",
              'Boston':"sunny",
              'los angelos':"cloudy"}

sunny_weather = {key : value for (key,value) in dictionnary.items() if value=="sunny"}

print(sunny_weather)

#if else

cities ={'martil':40,'tetouan':38,'tanger':23,'casa':10}

desc_cities = {key :("warm" if value >= 30 else "cold") for (key,value) in cities.items() }

print(desc_cities)


# using function

cities2 ={'martil':40,'tetouan':38,'tanger':23,'casa':10,'rabat':5}

def func(value):
    return "warm" if value >= 30 else "cold"

desc_cities2 = {key : func(value) for (key,value) in cities2.items() }

print(desc_cities2)