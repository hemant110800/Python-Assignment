people={1:{'name':'Rohit','age':27,'sex':'Male'},2:{'name':'Maria','age':30,'sex':'Female'}}
#Simple operations on nested dictionary
print(people)
print(people[1])
print(people[1]['name'])
print(people[2]['sex'])

#to add new element in dictionary
people[3]={}
people[3]['name']='Maria'
people[3]['sex']='Female'
people[3]['age']=25
people[3]['married']="no"
print(people[3])

#Another way to create new dictionary
people[4]={'name':'Peter','age':40,'sex':'Male'}
print(people)

#Delete specific elements of dictionary
del people[3]['sex']
del people[3]['married']
print(people[3])

#Modifying the dictionary using the deletion and insertion operation
people[3]['sex']='Female'
del people[3]
print(people)


#Iterating through dictionary
for pid,pinfo in people.items():
    print("\nPersion id-",pid)
    for key in pinfo:
        print(key,":",pinfo[key])


