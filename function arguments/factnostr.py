#sum of factorials of each digit of the number ==strong_num
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

def strong(num):
    res=0
    while num:
        last_digit=get_last_digit(num)
        res = add(res,factorial(last_digit))
        num = remove_last_digit(num)
    return res

def is_strong():
    num=int(input('enter the number='))
    if num == strong(num):
        print(f'{num} is a strong number')
    else:
        print(f'{num} is not a strong number')
