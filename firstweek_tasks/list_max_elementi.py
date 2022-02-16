# Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin.
my_list = input('list elementlerin daxil edin: ')
my_array = list(map(int,my_list.split()))
max_eded =len(my_array)
my_array.sort()
print('Listin en boyuk elementi:',my_array[max_eded-1])


  
