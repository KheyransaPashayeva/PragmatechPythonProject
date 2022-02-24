#Kvadrat tenliyi hell eden funksiya yazin (Kvadrat tenliyi research edin eger bilmirsize)
import math
emsallar = input('kvadrat tenliyin emsallarini daxil edin: ')
my_array = list(map(int,emsallar.split()))
a=my_array[0]
b=my_array[1]
c=my_array[2]
D = b * b -4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print(f'Tenliyinin kokleri x1= {x1},x2 = {x2}')
elif D==0:
    x1 = -b/(2*a)
    print(f'Tenliyin kokleri x1=x2={x1}')
elif D<0:
    x1=(-b + complex(i(math.sqrt(-b*b+4*a*c)))/(2*a))
    x2=(-b - complex(i(math.sqrt(-b*b+4*a*c)))/(2*a))
    print(f'Tenliyin heqiqi koku yoxdur!Bu halda tenliyin 2 kompleks koku var x1={x1},x2={x2}')