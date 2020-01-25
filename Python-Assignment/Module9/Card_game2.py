import random
class Hand:
    def __init__(self):
        self.__cards=[]
        self.__value=0

    def draw_from(self,deck):
        c=deck.return_cards()
        (self.__cards).append(c)
        self.__value=self.__value+c.get_value()
    def return_value(self):
        return self.__value
    def return_to(self,deck):
        c=self.__cards.pop(-1)
        self.__value=self.__value-c.get_value()
        deck.next_card(c)
    def __str__(self):
        for i in self.__cards:
            for j in i.__str__():
                print(j,end=' ')
            print()

class Card:
    __Faces=[]

    def __init__(self,face,suit,value):
        self.__face=face
        self.__suit=suit
        self.__value=int(value)
        self.__Faces.append(self.__face)
        self.__Faces.append(self.__suit)
        self.__Faces.append(self.__value)
    def get_value(self):
        return self.__value
    def __str__(self):
        return self.__Faces        

class Deck:
    def __init__(self):
        self.__cards=[]
    def shuffle(self):
        random.shuffle(self.__cards)

    def next_card(self,card):
        self.__cards.append(card)

    def return_cards(self):
        return self.__cards.pop(-1)

class Player:
    def __init__(self,name,credit):
        self.__name=name
        self.__credits=credit
        self.hand=Hand()
        self.__states=[]
    def play(self,deck,limit):
        if int((self.hand).return_value())>limit:
            print(self.__name," -: I am The Winner")
            return True
        #elif (self.__hand).return_value()==limit:
        else:
            (self.hand).draw_from(deck)
            (self.hand).__str__()
            print((self.hand).return_value())
            return False
    def show_hand(self):
        (self.__hand).__str__()
    def hit_or_stand(self):
        print("1.Hit")
        print("2.Stand")
        a=int(input("Press 1 or 2 -: "))
        if a==1:
             print("Hit me") 
        elif a==2:
            print("Pass")
        else:
            self.hit_or_stand()
class Game:
    def __init__(self,player,deck,dealer_name):
        self.__dealer="Kanha Gupta"
        self.player=Player(self.__dealer,300)
        self.deck=deck
        self.__players=player
        self.__history=[]
    def play_game(self):
        print(self.__players," is playing ")
        
        return (self.player).play(self.deck,21)

    def get_bust_probability():
        pass

name=input("Enter Your Name -: ")
ls=[['A','spade',16],
        ['4','club',4],
        ['J','heart',11],
        ['9','spade',9],
        ['A','diamond',16],
        ['10','spade',10],
        ['2','heart',2],]
deck=Deck()
for i in ls:
    card=Card(i[0],i[1],i[2])
    deck.next_card(card)
deck.shuffle()
game=Game(name,deck)
while True:        
    if game.play_game():
        break
