ch=1
while ch==1:
    print("menu")
    print("Addition")
    print("Subtraction")
    print("multiplication")
    print("Division")
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    c=int(input("Enter your choice 1/2/3/4:"))
    if c==1:
        print(f"{a}+{b}=",a+b)
    elif c==2:
        print(f"{a}-{b}=",a-b)
    elif c==3:
        print(f"{a}*{b}=",a*b)
    elif c==4:
        print(f"{a}5%{b}=",a/b)
    else:
        print("invalid choice")
    ch=int(input("Do you want to continue 0/1:"))
        
        