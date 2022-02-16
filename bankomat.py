n = input('Cixartmaq istediyiniz meblegi qeyd edin: ')
say=0
i=0
s=int(n)
while i < s:
    s=s
    if s >= 500:
        s=s-500
        say +=1
    elif s < 500 and s >= 200:
        s = s - 200
        say +=1 
    elif s >= 100 and s < 200:
        s -= 100
        say +=1
    elif s >= 50 and s < 100:
        s -= 50
        say += 1
    elif s >= 20 and s < 50:
        s -= 20
        say += 1
    elif s >= 10 and s < 20:
        s -= 10
        say += 1
    elif s < 10:
        print(-1)
    i +=1
print('mumkun helller sayi:',say,'qaliq qaytarila bilmeyen mebleg:',s)