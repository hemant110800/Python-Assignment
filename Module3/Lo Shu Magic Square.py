order=int(input("Enter order for magic square"))
mgsqr=[];sum2=0;sum3=0;sum4=0
ord2=order
while(order):
    lst=list(map(int,input().split()))
    mgsqr.append(lst)
    order-=1
sum1=sum(mgsqr[0])
for i in range(len(mgsqr)):
    if(sum(mgsqr[i])!=sum1):
        print("False:-Sorry the entered matrix is not a magic square")
        break
    for j in range(len(mgsqr)):
        sum2+=mgsqr[j][i]
        if(i==j):
            sum3+=mgsqr[i][j]
    if(sum2!=sum1):
        print("False:-Sorry the entered matrix is not a magic square")
        break
    sum4+=mgsqr[ord2-1-i][i]
    sum2=0
if(sum3==sum1 and sum4==sum1):
    print("The given square is magic square")
else:
    print("False:-Sorry the entered matrix is not a magic square")

    
        

    
