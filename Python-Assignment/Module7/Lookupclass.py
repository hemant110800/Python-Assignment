import pickle

class Contact:
    def __init__(self,name,phone,email):
        self.__name=name
        self.__phone=phone
        self.__email=email
    def set_name(self,name):
        self.__name=name
    def set_phone(self,phone):
        self.__phone=phone
    def set_email(self,email):
        self.__email=email
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_email(self):
        return self.__email
    def __str__(self):
        return f" The {self.__name} phone_number:-{self.__phone} and email:-{self.__email}"

fread=open("Lookup_pickel.dat",'rb')
dict1=pickle.load(fread)
fread.close()


def save():
    fopen=open("Lookup_pickel.dat",'wb')
    pickle.dump(dict1,fopen)
    fopen.close()



def lookup():
    id_customer=int(input("enter the id whose contact details you want"))
    count=1
    for i in dict1.keys():
        if(i==id_customer):
            count=0
            print("name:-",dict1[i].get_name())
            print("phoneno:-",dict1[i].get_phone())
            print("email:-",dict1[i].get_email())
    if(count):
        print("Record not exist")

    
def add():
    con2=Contact(input("CustomerName:-"),input("Phoneno:-"),input("Email:-"))
    dict1[len(dict1)+1]=con2
    
def update():
    try:
        id_customer=int(input("enter the id whose contact details you want to update"))
        if(not dict1[id_customer]):
            raise KeyError
        print("Enter the updated value for only those details those you want to update else None")
        name=input("NewName:-")
        phoneno=input("NewPhoneno:-")
        email=input("Newemail")
        
        if(name!='None'):
            dict1[id_customer].set_name(name)
        if(phoneno!='None'):
            dict1[id_customer].set_phone(phoneno)
        if(email!='None'):
            dict1[id_customer].set_email(email)
    except KeyError:
        print("Id not exist")

def total():
    print(len(dict1))

def list_id():
    l1=[i for i in dict1.keys()]
    print(l1)
        
    
def delete():
    try:
        id_customer=int(input("enter the id whose contact details you want to delete"))
        if(not dict1[id_customer]):
            raise KeyError
        del(dict1[id_customer])
    except KeyError:
        print("Id not exist")

def choice_of_user(choice):
    try:
        if(choice==1):
            lookup()
        elif(choice==2):
            add()
        elif(choice==3):
            update()
        elif(choice==4):
            delete()
        elif(choice==5):
            total()
        elif(choice==6):
            list_id()
        elif(choice==7):
            save()
        else:
            print("Invalid choice")
    except:
        print("Some error has reached")
        
def main():
    print("Hello user!\nOptions Available")
    print("\n0.Quit the program")
    print("1.Lookup a contact in the dictionary") 
    print("2.Add a new contact to the dictionary")
    print("3.Change an existing contact in the dictionary")
    print("4.Delete a contact from the dictionary")
    print("5.To see total id's(records) in dictionary")
    print("6.To see list of id's(records) in dictionary")
    print("7.Save the content")
    choice=-1
    while(choice):
        choice=int(input("\nPlease enter your choice "))
        if(not choice):
            continue
        choice_of_user(choice)

main()
