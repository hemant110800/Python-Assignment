import pickle

class Myexception(Exception):
    pass

in_file=open('datastore.dat','rb')
datastore=pickle.load(in_file)
in_file.close()
#---------------#--------------#--------------#-#-ADD Functions[which add the fields and field values]--#-#-----------#-------     
def save():
    otfile=open('datastore.dat','wb')
    pickle.dump(datastore,otfile)
    otfile.close()

def new_office():
    name=input("Next-Office")
    try:
        if(name.isdigit()):
            raise Myexception
        datastore[name]=datastore["office"]
    except Myexception:
        print("Enter name of office")

def add_field():
    try:
        name=input("OfficeName:-")
        if(not datastore[name]):
            raise KeyError
        field_name=input("FieldName:-") 
        if(field_name.isdigit()):
            raise Myexception
        datastore[name][field_name]=list()
        print("The",field_name,"is added")
    except KeyError:
        print("Enter the correct office that exist in dictionary")
    except Myexception:
        print("Enter name of Field")
    except:
        print("Error reached")
    
    
def add_field_values():
    try:
        name=input("OfficeName:-")
        if(not datastore[name]):
            raise KeyError
        field_name=input("FieldName:-")
        count=int(input("Number of values"))
        for i in range(count):
            str1=""
            new_dict={}
            new_dict['room_number']=int(input("RoomNo:-"))
            for k in range(len(datastore[name][field_name])):
                if(new_dict['room_number']==datastore[name][field_name][k]['room_number']):
                    str1="Room number already exists!"
                    print(str1)
                    break
            if(str1!="Room number already exists!"):
                new_dict['use']=input("Use:-")
                new_dict['sq-ft']=input("Size:-")
                new_dict['price']=int(input("Price:-"))
                datastore[name][field_name].append(new_dict)
    except KeyError:
        print("Enter the correct keys that exist in dictionary")
    except:
        print("Error reached")
              

#---------------#--------------#--------------#-#-Room Counter Function[which counts the total number of rooms]--#-#-----------#--------------#--------------#   

def room_count():
    try:
        name=input("OfficeName:-")
        if(not datastore[name]):
            raise KeyError
        field_name=input("FieldName:-")
        if(not datastore[name][field_name]):
            raise KeyError
        if(field_name!='parking'):
            print("The total number of rooms in",field_name,len(datastore[name][field_name]))
    except KeyError:
        print("Enter the correct keys that exist in dictionary")
    except:
        print("Error reached")

#---------------#--------------#--------------#-#-Show Functions[which show the specific element]--#-#-----------#--------------#--------------#   

def show_price_room():
    try:
        name=input("OfficeName:-")
        if(not datastore[name]):
            raise KeyError
        field_name=input("FieldName:-")
        if(not datastore[name][field_name]):
            raise KeyError
        room=int(input("RoomNo:-"))
        count=0
        for i in range(len(datastore[name][field_name])):
            count+=1
            for j in datastore[name][field_name][i].keys():
                if(datastore[name][field_name][i][j]==room):
                    count-=1
                    print(datastore[name][field_name][i]['price'])
                    break      
        if(count==len(datastore[name][field_name])):
            print("Room Number not exist")
    except KeyError:
            print("Enter the correct keys that exist in dictionary")
    except:
            print("Error reached")

def show_room_usage():
    try:
        name=input("OfficeName:-")
        if(not datastore[name]):
            raise KeyError
        field_name=input("FieldName:-")
        if(not datastore[name][field_name]):
            raise KeyError
        room=int(input("RoomNo:-"))
        count=0
        for i in range(len(datastore[name][field_name])):
            count+=1
            for j in datastore[name][field_name][i].keys():
                if(datastore[name][field_name][i][j]==room):
                    count-=1
                    print(datastore[name][field_name][i]['use'])
                    break
        if(count==len(datastore[name][field_name])):
            print("Room Number not exist")
    except KeyError:
            print("Enter the correct keys that exist in dictionary")
    except:
            print("Error reached")


#---------------#--------------#--------------#-#-Set Functions[which change the values according to user needs]--#-#-----------#--------------#--------------#            
def set_price_room():
    try:
        name=input("OfficeName:-")
        if(not datastore[name]):
            raise KeyError
        field_name=input("FieldName:-")
        if(not datastore[name][field_name]):
            raise KeyError
        room=int(input("RoomNo:-"))
        count=0
        updated=int(input("NewPrice:-"))
        for i in range(len(datastore[name][field_name])):
            count+=1
            if(datastore[name][field_name][i]["room_number"]==room):
                count-=1
                datastore[name][field_name][i]["price"]=updated
    except KeyError:
            print("Enter the correct keys that exist in dictionary")
    except:
            print("Error reached")

def set_location():
    try:
        name=input("OfficeName:-")
        newloc=input("New CarParking Location")
        datastore[name]["parking"]["location"]=newloc
    except KeyError:
            print("Enter the correct keys that exist in dictionary")
    except:
            print("Error reached")

def set_style():
    try:
        name=input("OfficeName:-")
        newstyle=input("New CarParking Style")
        datastore[name]["parking"]["style"]=newstyle
    except KeyError:
            print("Enter the correct keys that exist in dictionary")
    except:
            print("Error reached")

def set_parkingprice():
    try:
        name=input("OfficeName:-")
        newprice=int(input("NewPrice"))
        datastore[name]["parking"]["price"]=newprice
    except KeyError:
            print("Enter the correct keys that exist in dictionary")
    except:
            print("Error reached")
        

def set_size_room():
    try:
        name=input("OfficeName:-")
        field_name=input("FieldName:-")
        room=int(input("RoomNo:-"))
        updated=int(input("NewSize[sq-ft]:-"))
        for i in range(len(datastore[name][field_name])):
            if(datastore[name][field_name][i]["room_number"]==room):
                datastore[name][field_name][i]["sq-ft"]=updated
    except KeyError:
            print("Enter the correct keys that exist in dictionary")
    except:
            print("Error reached")
def set_roomno():
    try:
        name=input("OfficeName:-")
        field_name=input("FieldType:-")
        room_no=int(input("OldRoomNo:-"))
        newroom=int(input("NewRoomNo:-"))
        for i in range(len(datastore[name][field_name])):
            if(datastore[name][field_name][i]["room_number"]==room_no):
                datastore[name][field_name][i]["room_number"]=newroom
                datastore[name][field_name][i]["price"]=int(input("NewPrice"))
                datastore[name][field_name][i]["use"]=input("NewUse")
                datastore[name][field_name][i]["sq-ft"]=int(input("NewSize:-"))
    except KeyError:
            print("Enter the correct keys that exist in dictionary")
    except:
            print("Error reached")

#---------------#--------------#--------------#-#-function to Print The Data--#-#-----------#--------------#--------------#

def print1():
    print(datastore)
    print('\n\nNo. of Offices \t Fields\n')
    print("---------------------------------------------------------")
    try:
        for i in datastore:
            print(i.ljust(20),end='')
            for j in datastore[i]:
                print(j.ljust(20),end='')
            print()
            print()
            for j in datastore[i]:
                if j!="parking" and len(datastore[i][j])!=0:
                    l=[i  for i in datastore[i][j][0]]
                    for m in range(len(l)):
                        print(str(l[m]).ljust(20),end='' )
                    print()
                    for x in range(len(datastore[i][j])):
                        for k in l:
                            print(str(datastore[i][j][x][k]).ljust(20),end=' ')
                        print()
                    print()
                elif(j=="parking"):
                    l=[i  for i in datastore[i][j]]
                    for m in range(len(l)):
                        print(str(l[m]).ljust(20),end='' )
                    print()
                    for k in l:
                        print(str(datastore[i][j][k]).ljust(20),end=' ')
                    print()
                    print()
        print("-------------------------------------------------------------------------------------------")
    except Exception as error:
        print("Some error has reached")



#---------------#--------------#--------------#-#-Delete Functions[Office,Field,sub-fields]--#-#-----------#--------------#--------------#

def delete_office():
    try:
        name=input("OfficeName:-")
        del(datastore[name])
    except KeyError:
        print("Please check your key")
    except:
        print("Error reached")

def delete_field():
    try:
        name=input("OfficeName:-")
        field_name=input("FieldType:-")
        del(datastore[name][field_name])
    except KeyError:
        print("Check your keys")
    except:
        print("Error reached")

def delete_field_values():
    try:
        name=input("OfficeName:-")
        field_name=input("FieldType:-")
        sub_field=input("SpecificFieldValue:-")
        if(sub_field=='room_number'):
            room_no=int(input("Roomno"))
            for i in range(len(datastore[name][field_name])):
                if(datastore[name][field_name][i]["room_number"]==room_no):
                    del(datastore[name][field_name][i]['room_number'])
                    break
        elif(sub_field=='price'):
            room_no=int(input("Roomno"))
            for i in range(len(datastore[name][field_name])):
                if(datastore[name][field_name][i]["room_number"]==room_no):
                    del(datastore[name][field_name][i]['price'])
                    break
        elif(sub_field=='use'):
            room_no=int(input("Roomno"))
            for i in range(len(datastore[name][field_name])):
                if(datastore[name][field_name][i]["room_number"]==room_no):
                    del(datastore[name][field_name][i]['use'])
                    break
        elif(sub_field=='sq-ft'):
            room_no=int(input("Roomno"))
            for i in range(len(datastore[name][field_name])):
                if(datastore[name][field_name][i]["room_number"]==room_no):
                    del(datastore[name][field_name][i]['sq-ft'])
                    break
        else:
            del(datastore[name][field_name][sub_field])
    except KeyError:
        print("Check your keys")
    except:
        print("Error reached") 
        
#---------------#--------------#--------------#-#-Choice Function which call the function according to the need--#-#-----------#--------------#--------------#    

def choice_of_user(choice):
    if(choice==1):
        add_field()
    elif(choice==2):
        add_field_values()
    elif(choice==3):
        show_price_room()
    elif(choice==4):
        show_room_usage()
    elif(choice==5):
        set_location()
    elif(choice==6):
        set_style()
    elif(choice==7):
        set_parkingprice()
    elif(choice==8):
        room_count()
    elif(choice==9):
        set_price_room()
    elif(choice==10):
        set_size_room()
    elif(choice==11):
        set_roomno()
    elif(choice==12):
        print1()
    elif(choice==13):
        new_office()
    elif(choice==14):
        delete_office()
    elif(choice==15):
        delete_field()
    elif(choice==16):
        delete_field_values()
    elif(choice==17):
        save()
    else:
        print("Invalid Choice")
        
    
#---------------#--------------#--------------#-#-Options For Users--#-#-----------#--------------#--------------#
       
def main():
    try:
        print("Hello user!\nOptions Available")
        print("\n0.To exit the loop")
        print("1.Add the extra field in office")
        print("2.To add the room_number[unique],use,size and price in any field")
        print("3.Get the price of particular room in particular field")
        print("4.To know the use of room in fields of office")
        print("5.To change the location of parking area")
        print("6.To change the style of parking area")
        print("7.To change the price of parking area according to its location")
        print("8.Total number of rooms in particular field of office")
        print("9.To set the price of room")
        print("10.To set the size(sq-ft) of room")
        print("11.To change room-number")
        print("12.To display dictionary")
        print("13.To enter another office")
        print("14.Delete the entire office type")
        print("15.Delete Specific Field")
        print("16.Delete Specific field-value")
        print("17.Save the content!")
        choice=-1
        while(choice):
            choice=int(input("\nPlease enter your choice "))
            if(not choice):
                continue
            choice_of_user(choice)
    except:
        print("Please enter choice properly")

main()
