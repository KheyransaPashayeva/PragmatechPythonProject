# Write a Python program to check a list is empty or not.
my_list = input('list elementlerin daxil edin: ')
my_array = list(map(int,my_list.split()))
if len(my_array) >0:
    print('list bos deyil')
else:
   print('list bosdur')