def is_perfect():
    num=int(input('enter a number='))
    if num==sum_of_proper_factor(num):
        print(f'{num} is a perfect number')
    else:
        print(f'{num} is not a perfect number')

def sum_of_proper_factor(num):
    res=0
    for n in range(1,num):
        if not divisible(num,n):
            res=add(res,n)
    return res

def divisible (num1,num2):
    return (num1%num2)

def add(num1,num2):
    return num1+num2
