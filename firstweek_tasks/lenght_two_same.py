 #Write a Python program to count the number of strings where the string length is 2 or
#  more and the first and last character are same from a given list of strings.
#  Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2
my_list = ['abc', 'xyz', 'aba', '122','4gf5','2j2','fbhhbf','bfhfjjhb']
say = 0
for i in my_list:
    if len(i) > 1 and i[0]==i[-1]:
        say +=1
print(say)