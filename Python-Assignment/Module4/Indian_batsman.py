n=int(input("Enter number of players"))
ind_bat={}
types=input("Enter the type of player")
ind_bat[types]={}
for plyr in range(n):
    if(plyr!=0):
        tp=input("Enter the type of player")
        if(tp!=types):
            types=tp
            ind_bat[types]={}
    name=input("Name of player")
    ind_bat[types][name]={}
    ind_bat[types][name]['Matches']=int(input("Total number of matches played by player"))
    ind_bat[types][name]['Runs']=int(input("Total number of runs"))
    ind_bat[types][name]['Average']=float(input("Average number of runs by player"))
    ind_bat[types][name]['Highest_Score']=int(input("Highest score out of all matches by player"))
print(ind_bat)

new_dict={}
for types in ind_bat.keys():
    for name in ind_bat[types].keys():
        new_dict[ind_bat[types][name]['Highest_Score']]=name
print(new_dict[sorted(new_dict,reverse=True)[0]])

