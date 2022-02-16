# Listin en kicik elementini min funksiyasini istifade etmededen tapan alqoritm yazin.
my_list = input('List elementlerin daxil edin: ')
my_array = list(map(int,my_list.split()))
max_eded =len(my_array)
my_array.sort()
print('Listin en kicik elementi:',my_array[0])