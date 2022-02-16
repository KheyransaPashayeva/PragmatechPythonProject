#Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. Adın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.
# Əgər adını düzgün daxil edərsə, soyadının daxil etməsini istəyin. Soyad 5 hərfdən kiçik,
#  15 hərfdən uzun olmasın. Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin.
#  Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır. Sonra email daxil etməsini tələb edin. 
# Emailin uzunluğu 10 hərifdən qısa 22 hərfdən uzzun olmasın, tərkibində @gmail.com olsun və bu hissə 
# daxil etdiyi emailin sonunda olsun. Ardınca parol axil etsin. Parol 6-13 simvol aralığında olmalıdır.
#  Sonra parolu təsdiqləməyini tələb edin. Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır.
#  Bütün bunlar düzgün daxil edilərsə, Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın
#  detallarına baxmaq istəyib-istəməməsi soruşulsun. Əgər hə desə, aşağıdakı görüntü çapa verilsin: 
# (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə, hər verdiyibiz şərtə
#  uyğun error tipli mesaj verin. Məsələn doğum ilini 5 simvoldan ibarət daxil etsə, mesaj verilsin ki 4 
# simvol daxil edin. Yəni hər şərti müvafiq mesajlar ilə userə izah edin.
# Ad: Murad Soyad: Əliyev Yaş: 22 Email: muradaliyev1996@gmail.com Parol: 123456789 
#  Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın.
ad = input('Ad daxil edin: ')
email = '@gmail.com'
if len(ad) > 3 and len(ad) < 11 :
    soyad = input('Soyad daxil edin: ')
    if len(soyad) > 5 and len(soyad) < 15 :
        il = input('Doguldugunuz ili daxil edin: ')    
        if len(il) == 4 :
            mail = input('email daxil edin: ')
            bolgu = mail.split('@')
            if len(mail) >10 and len(mail) < 22 and email in mail  and bolgu[1] == 'gmail.com':
                parol = input('Parol daxil edin: ')
                if len(parol) > 6 and len(parol)< 13:
                    tesdiq = input('Parolu tesdiqle: ')
                    if parol == tesdiq :
                        print('Qeydiyyat tamamlandi!')
                        yoxla = input('Qeydiyyat detallarini gormek isteyirsiz? ')
                        if yoxla == 'he':
                            print(f'Ad: {ad} Soyad: {soyad} Yas: {il} Email: {mail} Parol: {parol}')
                        elif yoxla == 'yox':
                            print('Murad Əliyev, Uğurlar!')
                    else:
                       print('Parol tesdiq duzgun daxil edilmeyib!')
                else:
                    print('parol duzgun daxil edilmeyib!')
            else:
                print('mail duzgun daxil edilmeyib!')
        else:
           print('Il duzgun daxil edilmeyib!')   
    else:
        print('Soyad duzgun daxil edilmeyib!')

else:
    print('Ad duzgun daxil edilmeyib!')