filename=input("Enter your full path of file")
spl=list(filename)
ind=spl.index(".")
print("".join(i for i in spl[ind+1:]))
