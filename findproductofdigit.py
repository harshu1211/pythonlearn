i=int(input("enter your value:-"))
pro=1
while(i>0):
    pro=pro*(i%10)
    i=i//10
    print(pro)
