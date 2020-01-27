import random

#---------------------Card class which contain card details------------------------#
class Card:   
    def __init__(self,face,suit,value):
        self.face=face
        self.suit=suit
        self.value=value
        
    def __str__(self):
        return f'{self.face} {self.suit} {self.value}'

#---------------------Deck class which contain deck of 52 cards----------------------#
        
class Deck:
    def __init__(self):
        card_details=''
        
    #Shuffling of card

    def shuffle(self,list_of_cards):
        card_details=random.shuffle(list_of_cards)
        
    #We choose next card from list of cards available

    def next_card(self):
        card_details=random.choice(list_of_cards)
        print(card_details)
        return card_details

    #return the list of cards available
    
    def return_cards(self):
        return list_of_cards

    #To add new card in list of cards available
    
    def addCard(self,list_of_cards,new_card):
        list_of_cards.append(new_card)  

#---------------------hand class which draws card from deck of cards-----------------------#

class Hand:
    def __init__(self):
        self.card_taken=''
        self.total_value=0

    #Hand draw card from deck of cards
        
    def drawn_from(self,hand_card,deck_of_card):        
        self.card_taken=deck_of_card.next_card()
        hand_card.append(self.card_taken)
        list_of_cards.remove(self.card_taken)
        self.total_value=int(self.card_taken.split()[2])
        return self.total_value

    #Again we put the card from hand to deck of cards
    
    def return_to(self):
        list_of_cards.append(self.card_taken)
        hand_card.remove(self.card_taken)
        self.total_value=int(self.card_taken.split()[2])
        return self.total_value

#---------------------Player class contain player details-----------------------#
    
class Player:
    def __init__(self,credit):
        self.name=input("Enter player name")
        self.credit=credit

    #It contain status of player whether he wants to play the game or not
        
    def play(self):
        return(int(input("Do you want to play?\nEnter 1 for yes and 0 for no")))

    #It shows the card present in hand
    
    def show_hand(self,hcard):
        print("Cards in hand",hcard)

    def stand(self):
        pass
        
        
                

list_of_cards=[]
hand_card=[]
total_value=0
deck1=Deck()


for suit in ['Club','Diamond','Spade','Heart']:
    for j in range(2,11):
        c=Card('None',suit,j)
        deck1.addCard(list_of_cards,c.__str__())
for suit in ['Club','Diamond','Spade','Heart']:
    for face in ['Jack','Queen','King','Ace']:
        if face=='Ace':
            value=1
        elif face=='King':
            value=13
        elif face=='Queen':
            value=12
        else:
            value=11
        c=Card(face,suit,value)
        deck1.addCard(list_of_cards,c.__str__())

p=Player(total_value)
hand=Hand()
count=0
while(p.play()):
    count+=1
    deck1.shuffle(list_of_cards)
    if(count==1):
        total_value+=hand.drawn_from(hand_card,deck1)+hand.drawn_from(hand_card,deck1)
    else:
        total_value+=hand.drawn_from(hand_card,deck1)
    if(int(input("Do you want to replace it in deck? Enter 1 or 0"))):
        total_value-=hand.return_to()       
        p.show_hand(hand_card)
    print(p.name,"credit:",total_value)
    if total_value>21:
        print("You won!Congrulations ",p.name)
        total_value=0
        count=0
print("Visit Again!Hope you enjoyed")
