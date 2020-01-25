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

#-----------Writing in file------------------------------------------#
def writing(ob1):
    fopen=open("contact_information.txt",'w')
    fopen.write(str(ob1.get_name())+"\n")
    fopen.write(str(ob1.get_phone())+"\n")
    fopen.write(str(ob1.get_email())+"\n")
    fopen.close()
    return("Your data is written to the file")
#-----------Reading in file------------------------------------------#

def reading():
    fread=open("contact_information.txt",'r')
    new_name=fread.readline()
    new_phone=fread.readline()
    new_email=fread.readline()
    return[new_name,new_phone,new_email]
    fread.close()

#-----------Updating the values and store in file---------------------#
def update(obj):
    obj.set_name("hemant bhati")
    obj.set_phone(9123003022)
    obj.set_email("yashashvi123@gmail.com")
    writing(obj)
    print(obj)

#-----------getting the new values from file---------------------#

def get():
    new_name,new_phone,new_email=reading()    
    men2=Contact(new_name,new_phone,new_email)
    print(men2)

men=Contact("Rahul",9176982345,"rahul12@gmail.com")

def choice_of_user(choice):
    if(choice==1):
        writing(men)
    elif(choice==2):
        get()
    elif(choice==3):
        update(men)
    else:
        print("Invalid choice")
        
print("Hello user!\nOptions Available")
print("\n0.To exit the loop")
print("1.Writing in file")
print("2.Reading from file")
print("3.Updating the file")
choice=-1
while(choice):
    choice=int(input("\nPlease enter your choice "))
    if(not choice):
        continue
    choice_of_user(choice)
 
