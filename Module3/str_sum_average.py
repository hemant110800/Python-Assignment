res=input()
spl1=res.split()
l2=[int(i.split("=")[1]) for i in spl1]
print("sum",sum(l2),"Percentage is",(sum(l2)/(len(l2)*100))*100)
