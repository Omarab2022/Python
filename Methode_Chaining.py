class car :
    def turn_on(self):
        print("1 : turn on the car")
        return self
    def drive(self):
        print("2 : drive the car")
        return self

    def brake(self):
        print("3 : brake the car")
        return self
    def turn_off(self):
        print("4 : turn off the car")
        return self

car = car()
car.turn_on().drive().brake().turn_off()