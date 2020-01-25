total=int(input("enter the no of fruits"))
fruit={}
for i in range(total):
    fruit[i+1]={}
    fruit[i+1]['name']=input("Enter the name of the fruit")
    fruit[i+1]['bionomical name']=input("Enter the bionomical name for fruit")
    count=int(input("enter how many major producers are available"))
    fruit[i+1]['major_producers']={}
    for j in range(count):
        x=input()
        fruit[i+1]['major_producers'][x]={}
        fruit[i+1]['major_producers'][x]['nutrition']={}
        fruit[i+1]['major_producers'][x]['nutrition']['carbohydrates']=float(input("enter carbohydrate of fruit"))
        fruit[i+1]['major_producers'][x]['nutrition']['fat']=float(input("enter fat in your fruit"))
        fruit[i+1]['major_producers'][x]['nutrition']['protein']=float(input("enter protein value"))
print(fruit)

l2=[];l1=[]
for fruit_id in fruit.keys():
    for nut in fruit[fruit_id]['major_producers'].keys():
        if(nut=="China"):
            l2.append(fruit[fruit_id]['major_producers'][nut]['nutrition']['protein'])
        l1.append(fruit[fruit_id]['major_producers'][nut]['nutrition']['protein'])
print("Maximum production among magor producer in protein is",max(l1))
print("Maximum production among magor producer in protein in China is",max(l2))
        
