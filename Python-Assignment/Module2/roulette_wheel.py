pocket=int(input("Enter a pocket number"))
if(pocket==0):
    print("green")
elif(pocket>=1 and pocket<=10):
    if(pocket%2==0):
        print("black")
    else:
        print("red")
elif(pocket>=11 and pocket<=18):
    if(pocket%2==0):
        print("red")
    else:
        print("black")
elif(pocket>=19 and pocket<=28):
    if(pocket%2==0):
        print("black")
    else:
        print("red")
elif(pocket>=29 and pocket<=36):
    if(pocket%2==0):
        print("red")
    else:
        print("black")
else:
    print("error")
