import winsound

number=(input("Enter your number:-"))
one_place={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
two_place={11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",
           19:"ninteen",1:"ten",2:"twenty",3:"thirty",4:"fourty",5:"fivty",6:"sixty",7:"seventy",8:"eighty",9:"ninty"}
digit={1:one_place,2:two_place,3:" hundred ",4:" thousand "}
s1=list(number)
length=len(s1)
str1=""
for i in s1:
    if(len(number)==1 and i=='0'):                #this program converts the number  into string format
        str1+=one_place[int(i)]
    if(i=='0'):
        length-=1
        continue
    if(length==2 and (int(number[-2:]) in range(11,20))):
        str1+=two_place[int(number[-2:])]
        break
    elif(length>=3):
        str1+=one_place[int(i)]+digit[length]
    else:
        overall=digit[length]
        str1+=overall[int(i)]+" "
    length-=1
print(str1)

if(str1=="seventy five "):                                                                #to hear other sounds we can download  and check sother .wav file
    winsound.PlaySound('70.wav', winsound.SND_FILENAME) 
    winsound.PlaySound('5.wav', winsound.SND_FILENAME)
elif(str1=="nine thousand nine hundred ninty nine "):
    winsound.PlaySound('9.wav', winsound.SND_FILENAME)
    winsound.PlaySound('thousand.wav', winsound.SND_FILENAME) 
    winsound.PlaySound('9.wav', winsound.SND_FILENAME)
    winsound.PlaySound('hundred.wav', winsound.SND_FILENAME)
    winsound.PlaySound('90.wav', winsound.SND_FILENAME)    
    winsound.PlaySound('9.wav', winsound.SND_FILENAME)
elif(str1=="four hundred fifty "):
    winsound.PlaySound('4.wav', winsound.SND_FILENAME)
    winsound.PlaySound('hundred.wav', winsound.SND_FILENAME)
    winsound.PlaySound('50.wav', winsound.SND_FILENAME) 
else:
    print("You can download other .wav files and check other sound")



'''
import winsound
n=int(input("Enter number"))
l=len(str(n))
d1={0:winsound.PlaySound('0.wav',winsound.SND_FILENAME),1:winsound.PlaySound('1.wav',winsound.SND_FILENAME),2:winsound.PlaySound('2.wav',winsound.SND_FILENAME),3:winsound.PlaySound('3.wav',winsound.SND_FILENAME),4:winsound.PlaySound('4.wav',winsound.SND_FILENAME),5:winsound.PlaySound('5.wav',winsound.SND_FILENAME),6:winsound.PlaySound('6.wav',winsound.SND_FILENAME),7:winsound.PlaySound('7.wav',winsound.SND_FILENAME),8:winsound.PlaySound('8.wav',winsound.SND_FILENAME),9:winsound.PlaySound('9.wav',winsound.SND_FILENAME)}
d2={10:winsound.PlaySound('10.wav',winsound.SND_FILENAME),11:winsound.PlaySound('11.wav',winsound.SND_FILENAME),12:winsound.PlaySound('12.wav',winsound.SND_FILENAME),13:winsound.PlaySound('13.wav',winsound.SND_FILENAME),14:winsound.PlaySound('14.wav',winsound.SND_FILENAME),15:winsound.PlaySound('15.wav',winsound.SND_FILENAME),16:winsound.PlaySound('16.wav',winsound.SND_FILENAME),17:winsound.PlaySound('17.wav',winsound.SND_FILENAME),18:winsound.PlaySound('18.wav',winsound.SND_FILENAME),19:winsound.PlaySound('19.wav',winsound.SND_FILENAME),20:winsound.PlaySound('20.wav',winsound.SND_FILENAME),30:winsound.PlaySound('30.wav',winsound.SND_FILENAME),40:winsound.PlaySound('40.wav',winsound.SND_FILENAME),50:winsound.PlaySound('50.wav',winsound.SND_FILENAME),60:winsound.PlaySound('60.wav',winsound.SND_FILENAME),70:winsound.PlaySound('70.wav',winsound.SND_FILENAME),80:winsound.PlaySound('80.wav',winsound.SND_FILENAME),90:winsound.PlaySound('90.wav',winsound.SND_FILENAME)}
if l==1:
    d1[0]
elif l==2:
    if n in d2:
        d2[n]
    else:
        a=n//10
        d2[a]
        r=n%10
        d1[r]
        print("sr")
By directly storing the sound in dictionary wecan play sounds of numbers

'''
