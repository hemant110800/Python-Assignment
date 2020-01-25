#----Left arrow for star pattern

n=int(input("Enter range for star pattern"))
for i in range(n):
    print("*"*(n-i))
for i in range(2,n+1):
    print("*"*i)
print("\n\n")

#----Plus star pattern
if(n%2==0):
    n+=1
for i in range(n):
    for j in range(n):
        if(n//2==j or n//2==i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print("\n\n")

#---Diamond star pattern

for i in range(0,n):
    if(i<n//2):
        print(str('  '*(n//2-i))+str('* '*(2*i+1))+str('  '*(n//2-i)))
    elif(i==n//2):
        print('* '*n)
    else:
        print(str('  '*(i-n//2))+str('* '*(2*n-2*i-1))+str('  '*(i-n//2)))
print("\n\n")
#---Hollow Pyramid star pattern
for i in range(n):
    for j in range(n):
        if((n//2-i)==0):
            st="*"*n
            print(st)
            break
        if(n//2-i==j or n//2+i==j):
            print("*",end="")
        else:
            print(" ",end="")
        
    print()

