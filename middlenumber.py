a=int(input("Enter your 1ST VALUE--"));
b=int(input("Enter your 2ND VALUE--"));
c=int(input("Enter your 3RD VALUE--"));
if(a>b and a<c)or (a<b and a>c):
    print(a,"is middle number");
elif(b>a and b<c)or (b<a and b>c):
    print(b,"is middle number");    
else:
    print(c,"is middle number");
