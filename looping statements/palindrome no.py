num=int(input("enter a number="))
temp=num
rev=0
while(num>0):
    ldig=num%10
    rev=rev*10+ldig
    num=num//10
if(temp==rev):
    print(f'{num} is palindrome')
else:
    print(f'{num} is not palindrome')
    
