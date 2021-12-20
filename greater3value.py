a=int(input("Enter your 1ST VALUE--"));
b=int(input("Enter your 2ND VALUE--"));
c=int(input("Enter your 3RD VALUE--"));
if a>b and a>c:
    print(a,"is greater than",b,",",c);
elif b>a and b>c:
    print(b,"is greater than",a,",",c);    
else:
    print(c,"is greater than",a,",",b);
