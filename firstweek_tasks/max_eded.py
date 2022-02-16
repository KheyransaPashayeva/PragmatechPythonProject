# Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.
eded = input('4 eded daxil edin: ')
ededler =eded.split()
my_ededler = list(map(int,ededler))
max_eded = max(my_ededler)
print('En boyuk eded =',max_eded)