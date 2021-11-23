def armstrong_numbers():
    num=int(input('enter to start the range='))
    num1=int(input('enter the end of range='))
    if num == range_armstrong(num):
        print(num,'are the amrstrong numbers')

def no_of_digits(num,num1):
    for num in range(num,num1):
        while num:
            num=add(num,1)
            num=remove_last_digit(num)
        return num

def add(num1,num2):
    return num1+num2

def get_last_digit(num):
    return num%10

def remove_last_digit(num):
    return num//10

def range_armstrong(num):
    sum=0
    temp=no_of_digits(num,num1)
    while num:
        last_digit=get_last_digit(num)
        res=add(res,last_digit**temp)
        num=remove_last_digit(num)
    return res
    


    
        

            


    
