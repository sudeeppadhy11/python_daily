import math

total=0
num=int(input('enter the number='))
temp=num
while(num):
    factorial=1
    i=1
    rem=num%10
    while(i<=rem):
        factorial=math.factorial(i)
        i=i+1
    total=total+factorial
    num=num//10
if (total==temp):
    print(f'{temp} is a strong number')
else:
    print(f'{temp} is not a strong number')
