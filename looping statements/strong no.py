total=0
num=int(input('enter a number='))
temp=num
while(num):
    fact=1
    i=1
    rem=num%10
    while(i<=rem):
        fact=fact*i
        i=i+1
    total=total+fact
    num=num//10
if (total == temp):
    print(f'{temp} is a strong number')
else:
    print(f'{temp} is not a strong number')
