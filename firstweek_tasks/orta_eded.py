
#Üç müxtəlif a, b, c ədədləri verilmişdir. Onlardan qiymətcə orta olanı tapın.
n = input('3 muxtelif eded daxil edin:')
s= list(map(int,n.split()))
i=0
if i== 0 and s[i] <= 1000:
  if s[i+1] < s[i] < s[i+2] or  s[i+1] > s[i] > s[i+2]:
    print('qiymetce orta olan eded:',s[i])
  if s[i] > s[i+1] and s[i] > s[i+2] and s[i+1] > s[i+2]:
    print('qiymetce orta olan eded:',s[i+1])
  if s[i] > s[i+1] and s[i] > s[i+2] and s[i+1] < s[i+2]:
    print('qiymetce orta olan eded:',s[i+2])
  if s[i]< s[i+1] and s[i] < s[i+2] and s[i+1] > s[i+2]:
    print('qiymetce orta olan eded:',s[i+2])
  elif s[i]< s[i+1] and s[i] < s[i+2] and s[i+1] < s[i+2]:
   print('qiymetce orta olan eded:',s[i+1])
else:
    print('daxil etdiyiniz ededler 1000-i asmamalidir!')