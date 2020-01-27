import pickle
dict1={}
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
def initial():
    count=int(input("TotalRecords:-"))
    for i in range(1,count+1):
        obj=Contact(input("CustomerName"),input("Phoneno:-"),input("Email:-"))
        dict1[i]=obj
    fopen=open("Lookup_pickel.dat",'wb')
    pickle.dump(dict1,fopen)
    fopen.close()


initial()

