print("Enter 0 product to break the loop\n")
while(1):
    prod=int(input("Enter number of product"))
    wholesale=input("Enter wholesale price of item")
    if(prod==0):
        break
    elif "-" in wholesale:
         continue
    else:
        retail=wholesale*0.5*prod
        print("Retail price of your item is ",retail)
        
    
