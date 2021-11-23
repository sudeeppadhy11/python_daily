import math

num=int(input('enter the number='))

temp=num

#count the number of digits
count = 0
while temp:
    count +=1
    temp//=10

#armstrong

temp=num
res=0
while temp:
    last_digit = temp %10
    res = res+pow(last_digit,count)
    temp//=10

if res==num:
    print(f'{num} is a armstrong number')
else:
    print(f'{num}is not a armstrong number')
