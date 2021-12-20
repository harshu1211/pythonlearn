a=int(input("Enter your 1ST VALUE--"));
b=int(input("Enter your 2ND VALUE--"));
c=int(input("Enter your 3RD VALUE--"));
d=int(input("Enter your 4TH VALUE--"));
e=int(input("Enter your 5TH VALUE--"));

total=a+b+c+d+e
print("your total score=",total);
percent=(total/500)*100
print("u have got",percent,"%");

if percent>=80:
    print("you have got A grade");
    
elif percent>=60:
    print("you have got B grade");
    
elif percent>=40:
    print("you have got C grade");

elif percent>=30:
    print("you have got D grade");

else:
    print("you are fail");
