class organisme :
    alive =True


class animal(organisme):
    def eat(self):
        print("animal is eating")


class dog(animal):
    def bar(self):
        print("this dog is barking")


class prey():
    def flee(self):
        print("this animal flees")

class predator():
    def hunt(self):
        print("this animal is hunt")

class lion(prey,predator):
    pass

dog = dog()
print(dog.alive)
dog.bar()
dog.eat()


lion = lion()
lion.hunt()
lion.flee()