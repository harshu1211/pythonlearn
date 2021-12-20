n=int(input("enter your value:-"))
i=n
count=0
while(i>0):
    count=count+1
    i=i//10
    print(count)
i=n
sum=0
while(i>0):
    digit=i%10
    x=1
    pro=1
    while(x<=count):
        pro=pro*digit
        x=x+1
    sum=sum+pro
    i=i//10
if(sum==n):
    print("armstrong")
else:
    print("its not")
    
