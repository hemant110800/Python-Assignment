lst1=list(map(int,input("Enter your list").split()))
uniq=list(set(lst1))
uniq.sort()
lst2=[lst1.count(i) for i in uniq]
while(max(lst2)!=-1):
    print((str(uniq[lst2.index(max(lst2))])+" ")*max(lst2),end="")
    if(len(lst2)!=0):
        lst2[lst2.index(max(lst2))]=-1
    
    
