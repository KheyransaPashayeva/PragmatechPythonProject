#Write a Python program to select the odd items of a list.
my_list = input('list elementlerin daxil edin: ')
my_array = list(map(int,my_list.split()))
for i in range(0,len(my_array)):
    if my_array[i] % 2 != 0:
        print(my_array[i])