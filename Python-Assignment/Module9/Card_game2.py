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
    
    def return_to(self,hand_card):
        list_of_cards.append(self.card_taken)
        hand_card.remove(self.card_taken)
        self.total_value=int(self.card_taken.split()[2])
        return self.total_value

#---------------------Player class contain player details-----------------------#
    
class Player:
    def __init__(self,credit,rec):
        self.name=input(f"Enter {rec+1} player name")
        self.credit=credit
        self.hc=[]

    #It contain status of player whether he wants to play the game or not
        
    def play(self):
        return(int(input("Do you want to play?\nEnter 1 for yes and 0 for no")))

    #It shows the card present in hand
    
    def show_hand(self,hcard):
        print("Cards in hand",hcard)

    def stand(self):
        pass
        
#--------------Game class plays the game between players till their score<21 and decide win accordingly---------------        

class Game:
    def __init__(self,pname):
        self.player=pname
    def play(self,n,d,s,h,u,hist):
        c=0
        while c!=n:
            print(self.player[c].name,"turn")
            d.shuffle(list_of_cards)
            s[c]+=h.drawn_from(self.player[c].hc,d)
            if(int(input("Do you want to replace it in deck? Enter 1 or 0"))):
                s[c]-=h.return_to(self.player[c].hc)     
                self.player[c].show_hand(self.player[c].hc)
                print(f"{self.player[c].name}, your total score is",s[c],"\n")
                if s[c]>21:
                    print(self.player[c].name," won\n")
                    hist.append(self.player[c].name+" won with score "+str(s[c]))
                    u[c]+=1
                    return -1
            else:
                self.player[c].show_hand(self.player[c].hc)
                print(f"{self.player[c].name}, your total score is",s[c],"\n")
                if s[c]>21:
                    print(self.player[c].name," won\n")
                    hist.append(self.player[c].name+" won with score "+str(s[c]))
                    u[c]+=1
                    return -1
                c+=1
        i=s.index(max(s))
        hist.append(self.player[i].name+" won with score "+str(s[i]))
        print(self.player[i].name," won\n")
        
    #It gives the probability of winning condition of players         
    def get_bust_probab(self,u,n,p):
        a=sum(u)
        for i in range(n):
            print("Probability of winning of ",self.player[i].name," is ",u[i]/a)
            self.player[i].hc.clear()

    #It gives the history of players which wons till the final match
    def get_history(self,hist):
        print("\nHistory of players:-")
        for i in range(len(hist)):                
            print(hist[i])
            
    
        
        

pname=[]                                                                        #Store object of players
n=int(input("Enter number of players "))
time_wins=[0]*(n+1)                                                                     #Store how many times a player wins
                                                                             
for rec in range(n):
    p=Player(0,rec)
    pname.append(p)
g=Game(pname)
while(int(input("Do you want to play? Enter 1/0"))):
    list_of_cards=[]                
    deck1=Deck()
    hand=Hand()
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

    player_score=[0]*(n+1)                                                                     #Stores score of a player                   
    hist=[]
    for i in range(10):
        status=g.play(n,deck1,player_score,hand,time_wins,hist)
        if status==-1:
            break
    g.get_bust_probab(time_wins,n,p)
    g.get_history(hist)
    
