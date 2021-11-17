#armstrong number
#no of digit in given number
#each no should be raised to the no of digits
def is_armstrong():
    num=int(input('enter the number='))
    if num == armstrong(num):
        print(f'{num} is a armstrong number')
    else:
        print(f'{num} is not a armstrong number')

def count_of_digit(num):
    count=0
    while num:
        count=add(count,1)
        num=remove_last_digit(num)
    return count
def add(num1,num2):
    return num1+num2

def get_last_digit(num):
    return num%10

def remove_last_digit(num):
    return num//10
        
def armstrong(num):
    res=0
    temp=count_of_digit(num)
    while num:
        last_digit= get_last_digit(num)
        res =add(res,last_digit**temp)
        num=remove_last_digit(num)
    return res
    


