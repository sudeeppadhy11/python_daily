def divisible(num):
    for i in range(2, (num//2)+1):
        if(num % i) == 0:
           print(num,'is not a prime number')
           break
    else:
         print(num,'is a prime number')            

def is_prime():
    num=int(input('enter the number='))
    if num > 1:
        divisible(num)
    else:
        print(num,'is a prime number')
