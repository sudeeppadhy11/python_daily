import operators
import countofdig
import math

def menu():
    print(f'1.Armstrong No')
    print(f'2.Armstrong No in range')
    print(f'3.Exit')
    choice=int(input('Enter the choice:'))
    if choice==1:
        is_armstrong()
    elif choice==2:
        armstrong_nos()
    elif choice==3:
        Exit
    else:
        print('Invalid choice')
        menu()
    



def is_armstrong():
    num=int(input('enter the number='))
    if num == armstrong(num):
        print(f'{num} is a armstrong number')
    else:
        print(f'{num} is not a armstrong number')
                                            

def armstrong(num):
    res=0
    temp=countofdig.count_of_digit(num)
    while num:
        last_digit=operators.get_last_digit(num)
        res =operators.add(res,math.pow(last_digit,temp))
        num=operators.remove_last_digit(num)
    return res
                  
#with range

def armstrong_nos():
    top=int(input('enter to start the range='))
    end=int(input('enter the end of range='))
    for num in range(top,end+1):
        if num==armstrong_number(num):
            print(num)
    
def armstrong_number(num):    
    sum=0
    temp=countofdig.count_of_digit(num)
    while num:
        last_digit=operators.get_last_digit(num)
        sum =operators.add(sum,math.pow(last_digit,temp))
        num=operators.remove_last_digit(num)
    return sum
    
