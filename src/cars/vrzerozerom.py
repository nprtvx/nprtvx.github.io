class Car:
    def __init__(self, car: Car=None, car_name: str=None):
        self.car = car
        self.car_name = car_name
    def drive(self):
        pass
    def create(self,user_name: str=None):
        pass
    def update(self):
        pass

if __name__=="__main__":
    car = Car()