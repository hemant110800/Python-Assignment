name=input("Please enter your name(kindly enter the space after the last character)")
final_list=[]
sub_list=[]

def print1(ind):
    print(" ".join(str(i) for i in ind),end="  ")
    
def print2(final_list):
    for j in range(0,3):
        for i in final_list:
            print1(i[j])
        print()
    print()
    final_list.clear()

def set_ch(ch):
    if(ch=='A'):
        sub_list=[[" ",1," "],[1,1,1],[1," ",1]]
        final_list.append(sub_list)
    elif(ch=='H'):
        sub_list=[[1," ",1],[1,1,1],[1," ",1]]
        final_list.append(sub_list)
    elif(ch=='E'):
        sub_list=[[1,1,1],[1,1," "],[1,1,1]]
        final_list.append(sub_list)
    elif(ch=='M'):
        sub_list=[[1," ",1],[1,1,1],[1," ",1]]
        final_list.append(sub_list)
    elif(ch=='N'):
        sub_list=[[1," ",1],[1,1,1],[1," ",1]]
        final_list.append(sub_list)
    elif(ch=='T'):
        sub_list=[[1,1,1],[" ",1," "],[" ",1," "]]
        final_list.append(sub_list)
    elif(ch=='D'):
        sub_list=[[1,1,1],[1," ",1],[1,1,1]]
        final_list.append(sub_list)

    


for ch in name:
    if(ch==' '):
        print2(final_list)
    else:
        set_ch(ch)

    
    
