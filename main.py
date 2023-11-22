import random
class Car:
    def __init__(self,registration_number,maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def show(self):
        return self.registration_number,self.maximum_speed,self.current_speed,self.travelled_distance
    def accelerate(self,speed):
        if self.current_speed+speed<self.maximum_speed and self.current_speed+speed>0:
            self.current_speed=self.current_speed+speed
            return 'speed updated'
        elif self.current_speed+speed<0:
            self.current_speed=0
        elif self.current_speed+speed<self.maximum_speed:
            self.current_speed=142
        else:
            return 'error'
    def drive(self,hours):
        if hours>0:
            self.travelled_distance=self.travelled_distance+self.current_speed*hours


#car_1=Car('ABC-123',142)
#car_1.accelerate(30)
#car_1.accelerate(70)
#car_1.accelerate(50)
#car_1.accelerate(-90)
#car_1.drive(1.5)
#print(car_1.show())
l=[Car('ABC-'+str(i),random.randint(100,200)) for i in range(10)]
t=0
while True:
    for i in l:
        i.accelerate(random.randint(-10,15))
        i.drive(t)
    t=t+1
    if i.travelled_distance>10000:
        break
#This code runs an iteration after a car reaches 10000 also so multiple cars may reach 10000
for i in l:
    print(i.show())
