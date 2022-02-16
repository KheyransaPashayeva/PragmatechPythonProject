# Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.
eded1 = int(input('eded daxil edin: '))
eded2 = int(input('eded daxil edin: '))
eded3 = int(input('eded daxil edin: '))
eded4 = int(input('eded daxil edin: ')) 
sahe=0
cem=0
if eded1 == eded2 == eded3 == eded4:
    sahe =eded1*eded2
    print('Kvadratin sahesi =',sahe)
elif eded1 != eded2:
    cem =eded1 + eded2 +eded3 + eded4
    print('Kvadrat yaratmaq olmaz, ededlerin cemi =',cem)