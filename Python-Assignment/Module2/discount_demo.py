packages=int(input("Enter the number of packages"))
amount=packages*99
if(packages>=100):
    discount=40
elif(packages>=50):
    discount=30
elif(packages>=20):
    discount=20
elif(packages>=10):
    discount=10
else:
    discount=0
if(discount):#if discount is 0 then no need to print amount of the discount.
    print("Amount of the discount $",amount*discount/100)
print("Total amount $",amount-(amount*discount/100))
