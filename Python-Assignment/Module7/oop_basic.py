import random
class Coin:
    def __init__(self):
        self.sideup='Heads'
    def toss(self):
        if(random.randint(0,2)==0):
            self.sideup='Heads'
        else:
            self.sideup='Tails'
    def get_sideup(self):
        return self.sideup

c1=Coin()
c1.toss()
print("this side is",c1.get_sideup())
c1.toss()
print("this side is",c1.get_sideup())
