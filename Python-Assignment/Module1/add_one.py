number=input("enter 5 digit number")
digits=list(number)
for i in range(len(digits)):
    if(int(digits[i])==9):
        digits[i]=0
    else:
        digits[i]=int(digits[i])+1
print("".join(str(i) for i in digits))
        
