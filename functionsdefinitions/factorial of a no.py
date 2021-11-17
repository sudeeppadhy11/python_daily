def factorial(num):
    fact=1
    for var in range(num,1,-1):
        fact*=var
    return fact
