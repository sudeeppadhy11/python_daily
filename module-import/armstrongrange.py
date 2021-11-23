import math
def armstrong_nos():
    top=int(input('enter to start the range='))
    end=int(input('enter the end of range='))
    for num in range(top,end+1):
        if num==armstrong(num):
            print(num)

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
    sum=0
    temp=count_of_digit(num)
    while num:
        last_digit=get_last_digit(num)
        sum =add(sum,math.pow(last_digit,temp))
        num=remove_last_digit(num)
    return sum
            
