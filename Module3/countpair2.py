sum1=int(input("enter sum you want"))
n1=list(map(int,input("Enter list1").split()))
n2=list(map(int,input("Enter list2").split()))
l1=[]
for i in n1:
    if(sum1-i) in n2:
        l1.append([i,sum1-i])
for i in l1:
    print("Possible Pair-",i)
