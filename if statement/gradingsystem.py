num=float(input('enter the marks='))
if num<=100 and num>=85:
    print('First class distinction wiht honor')
elif num<=84 and num>=70:
    print('First class distinction')
elif num<=69 and num>=60:
    print('First class')
elif num<=59 and num>=50:
    print('Second class')
elif num<=49 and num>=35:
    print('Pass')
elif num<=34:
    print('Fail')
else:
    print('supplementary exam')
