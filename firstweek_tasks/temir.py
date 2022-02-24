# uzunlugu L eni-W hundurluyu -H olan ve 1 bankanin 16 kvadratmetre kifayet edeceyini bilerek(ofisin pencere ve qapilari nezere alinmir)
# ofisin renglenmesine nece banka reng lazim oldugunu tapin.1-ci setrde sifarislerin sayi verilir,her 1 sifaris 1000 den boyuk
# olmamalidir.her 1 sifaris ucun ayri setirde ofis renglemek ucun nece banka reng lazimdir sayini vermeli.
n = int(input('sifaris sayini daxil edin: '))
say = 0
S=0
my_list=[]
for i in range(0,n):
    olculer = input('ofisin olculerini daxil edin: ')
    my_array = list(map(int,olculer.split()))
    L = my_array[0]
    W = my_array[1]
    H = my_array[2]
    S= L*W*H
    my_list.append(S)

for i in my_list:
    if i%16 ==0:
        say = i/16
    elif i%16 != 0:
        say = i/16 + 1
    print(int(say))