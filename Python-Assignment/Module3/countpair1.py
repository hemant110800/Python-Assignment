lst1=list(map(int,input("Enter the first list").split()))
lst2=[0 for i in range(max(lst1)+1)]
sum1=int(input("enter the sum you want"))
for i in range(0,len(lst1)):
    lst2[lst1[i]]=i
for i in range(0,len(lst1)):
    if(lst2[sum1-lst1[i]]!=i):
        if(lst2[sum1-lst1[i]]!=0):
            print(i," ",lst2[sum1-lst1[i]])
