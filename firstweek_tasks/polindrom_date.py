MAX_VALID_YR = 9999
MIN_VALID_YR = 1800
polindrom = []
next_polin_year=0
years =0
y1 = 2133
y2 = 2140
def isLeap(year):

    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

def isValidDate(d, m, y):
    if (y > MAX_VALID_YR or y < MIN_VALID_YR):
        return False
    if (m < 1 or m > 12):
        return False
    if (d < 1 or d > 31):
        return False
    if (m == 2):
        if (isLeap(y)):
            return (d <= 29)
        else:
            return (d <= 28)
    if (m == 4 or m == 6 or m == 9 or m == 11):
        return (d <= 30)
 
    return True
 
def printPalindromeDates(y1, y2):
    for year in range(y1, y2 + 1,1):
        str1 = str(year)
        rev = str1
        rev = rev[::-1]
        day = int(rev[0 : 2])
        month = int(rev[2 : 4])
        rev += str1
        if (isValidDate(day, month, year)):
            print(rev)   
            polindrom.append(rev)
    if len(polindrom)>1:
        next_polin_year = polindrom[1]
        years =int(next_polin_year[4:8])
        print(f'{y1} -ilinden', years-y1 , f'il sonra novbeti polindrom tarix {next_polin_year}')
    else:
        next_polin_year = polindrom[0]
        years =int(next_polin_year[4:8])
        print(f'{y1} -ilinden', years-y1 , f'il sonra novbeti polindrom tarix {next_polin_year}')
  
            
printPalindromeDates(y1, y2)



