import operators
import factorial
import math

def menu():
    print(f'1.Strong No')
    print(f'2.Strong No for range')
    print(f'3.Exit')
    choice=int(input('Enter the choice:'))
    if choice==1:
        is_strong()
    elif choice==2:
        is_strongno()
    elif choice==3:
        Exit
    else:
        print('Invalid')
        menu()


def is_strong():
    num=int(input('enter the number='))
    if num == strong(num):
        print(f'{num} is a strong number')
    else:
        print(f'{num} is not a strong number')


def strong(num):
    res=0
    while num:
        last_digit=operators.get_last_digit(num)
        res = operators.add(res,math.factorial(last_digit))
        num = operators.remove_last_digit(num)
    return res

#with range
def is_strongno():
    top=int(input('enter to start the range='))
    end=int(input('enter the end of range='))
    for num in range(top,end+1):
        if num==strongno(num):
            print(num)

def strongno(num):
    res=0
    while num:
        last_digit=operators.get_last_digit(num)
        res = operators.add(res,math.factorial(last_digit))
        num = operators.remove_last_digit(num)
    return res


