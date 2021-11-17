num1=int(input('enter the value for num1='))
num2=int(input('enter the value for num2='))
num3=int(input('enter the value for num3='))
if num1>=num2 and num1>=num3:
    print(num1,"is the greatest")
elif num2>=num3:
    print(num2,"is the greatest")
elif num3>=num1:
    print(num3,"is the greatest")
else:
    print("all the numbers are same")
