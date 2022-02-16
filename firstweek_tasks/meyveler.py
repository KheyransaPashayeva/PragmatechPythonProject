# Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun.
#  Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin 
# və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). 
# Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.
meyveler ={
    'alma':
    2,
    'ciyelek':
    3,
    'heyva':
    5,
    'gilas':
    2.3
}
def meyveler_list(kvars):
    my_list = kvars.keys()
    print('Meyveler menusu:',list(my_list))      
meyveler_list(meyveler)
meyve_sec = input('Meyve secin: ')
if meyve_sec in meyveler.keys():
    meyve_qiymet = meyveler.get(meyve_sec)
    print(f'{meyve_sec} -nin qiymeti: ',meyve_qiymet,'azn')
else:
    print('Daxil etdiyiniz meyve menusunde movcud deyil!')