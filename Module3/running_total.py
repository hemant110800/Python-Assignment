num=input().split()
n=int(num[0])
m=int(num[1])
fruit=list(map(int,input().split()))
l1=[];sum1=0
for x in range(n):
    i=-1
    while(i<m-1):
        i+=1
        sum1+=fruit[(x+i)%n]
    l1.append(sum1)
    sum1=0
print(max(l1))

        
    
