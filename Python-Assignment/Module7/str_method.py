class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return f'a {self.color} car'

mercidies=Car("Black",200)
print(mercidies)
