import Card_game1 as cd
nm=input('Enter Your name')
obj=cd.Player(nm)

while(obj.play()):
    obj.show_hand()
    pass
    
