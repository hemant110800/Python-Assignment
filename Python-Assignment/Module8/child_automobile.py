from automobile import Automobile
class Car(Automobile):
    def __init__(self,make,model,mileage,price,doors):
        Automobile.__init__(self,make,model,mileage,price)
        self.__doors=doors
    def set_doors(self,doors):
        self.__doors=doors
    def get_doors(self):
        return(self.__doors)

class Truck(Automobile):
    def __init__(self,make,model,mileage,price,drive_type):
        Automobile.__init__(self,make,model,mileage,price)
        self.__drive_type=drive_type
    def set_drive_type(self,drive_type):
        self.__drive_type=drive_type
    def get_drive_type(self):
        return(self.__drive_type)

class SUV(Automobile):
    def __init__(self,make,model,mileage,price,pass_cap):
        Automobile.__init__(self,make,model,mileage,price)
        self.__pass_cap=pass_cap
    def set_pass_cap(self,pass_cap):
        self.__pass_cap=pass_cap
    def get_pass_cap(self):
        return(self.__pass_cap)

Truck1=Truck("tata","234amegha","234","1200000","Non-ac")
print("Truck make:-",Truck1.get_make())
print("Truck model:-",Truck1.get_model())
print("truck mileage",Truck1.get_mileage())
Truck1.set_price("1300000")
print("Truck price:-",Truck1.get_price())
Car1=Car("tata","Swift","125","200000","2")
print("Car mileage",Car1.get_mileage())
