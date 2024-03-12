class organisme :
    alive =True


class animal(organisme):
    def eat(self):
        print("animal is eating")

class dog(animal):
    def bar(self):
        print("this dog is barking")


dog = dog()
print(dog.alive)
dog.bar()
dog.eat()