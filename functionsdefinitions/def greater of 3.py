x=int(input('enter the first number='))
y=int(input('enter the second number='))
z=int(input('enter the third number='))
def greater():
    if (x >=y) and (x >=z):
        print(x,"is the greatest")
    elif y>=z:
        print(y,"is the greatest")
    elif z>=x:
        print(z,"is the greatest")
    else:
        print("all are same")
greater()
