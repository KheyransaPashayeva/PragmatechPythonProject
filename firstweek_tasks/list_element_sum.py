# Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.

my_list = input('list elementlerin daxil edin: ')
my_array = list(map(int,my_list.split()))
cem =0
for i in my_array:
    cem += i
print('list elementlerinin cemi: ',cem)