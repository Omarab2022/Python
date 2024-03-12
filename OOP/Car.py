class Car :
    make = None
    model =None
    year=None
    color=None


    #constructor
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("drive the car : " + self.make + " , model : " + self.model + " , year : " + str(self.year))

    def stop(self):
        print("stop the car")

