def is_strongno():
    top=int(input('enter to start the range='))
    end=int(input('enter the end of range='))
    for num in range(top,end+1):
        if num==strong(num):
            print(num)
    

def factorial(num):
    fact=1
    for var in range(num,1,-1):
        fact*=var
    return fact

def add(num1,num2):
    return num1+num2

def get_last_digit(num):
    return num%10

def remove_last_digit(num):
    return num//10

def strongno(num):
    res=0
    while num:
        last_digit=get_last_digit(num)
        res = add(res,factorial(last_digit))
        num = remove_last_digit(num)
    return res
