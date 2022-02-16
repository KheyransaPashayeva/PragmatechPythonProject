#Write a Python function to multiply all the numbers in a list. Go to the editor
#  Sample List : (8, 2, 3, -1, 7) Expected Output : -336
my_list = input('list elementlerin daxil edin: ')
my_array = list(map(int,my_list.split()))
hasil =1
for i in my_array:
    hasil *= i
print('list elementlerinin hasili: ',hasil)