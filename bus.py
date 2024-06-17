class Vehicle():
    def __init__(self,max_speed,mileage,capacity):
        self.max_speed=max_speed
        self.mileage=mileage
        self.capacity=capacity
    def veh(self):
        print(self.mileage,"with speed of",self.max_speed)

    def capa(self):
        print(self.name, "has a capacity ", self.capacity)

    def fare(self):
        print(self.name, " fare is", self.capacity * 100)


class Bus(Vehicle):
    def __init__(self,name):
        self.name=name
    def details(self):
        print(self.name,"has a max speed of",self.max_speed,"with a mileage of ",self.mileage)
    def capacity(self):
        print(self.name,"has a capacity",50)
    def fare(self):
        print("Bus fare :",(50*100)+(50*100)/100)


vehicle=Bus("Bus")
vehicle.max_speed=200
vehicle.mileage=30
vehicle.details()
vehicle.capacity()
vehicle.fare()

