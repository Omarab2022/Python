class animal():
    def eat(self):
        print("animal is eating")

class dog(animal):
    def eat(self):
        print("dog is eating")

dog = dog()
dog.eat()