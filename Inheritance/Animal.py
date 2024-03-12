class animal :

    alive = True

    def eat(self):
        print("animal is eating")

    def sleep(self):
        print("this animal is sleeping")

class fish(animal):
    pass

animal1  = animal()
fish1 = fish()

animal1.eat()
fish1.eat()