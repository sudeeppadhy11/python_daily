def prime(num):
    for n in range(1,num):
        for i in range(2,n):
            if(n%i) == 0:
                break
        else:
            print(n)
def are_primeno():
    num=int(input('enter the number='))
    prime(num)
