number=int(input("enter a integer"))
leftshft=number<<1
if(number*2==leftshft):
    print("Multiplication by 2 is possible(left-shift)")
else:
    print("Multiplication by 2 is not possible")
    
rightshft=number>>1
if(number/2==rightshft):
    print("Division by 2 is posible(right-shift)")
else:
    print("Division is not possible")

