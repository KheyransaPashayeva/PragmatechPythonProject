from datetime import datetime, timedelta
import datedelta
import datetime

def checkIfPalindrome(string):
    length = len(string)
    even = length%2==0

    for i in range(int(length/2)):
        if string[i] != string[length-1 - i]:
            return False
    return True

def checkIfNumericPalindrome(number):
    return checkIfPalindrome(str(number))

def checkIfDateIsPalindrome(date):
    # day - month - year, no 0 padding
    if checkIfPalindrome('{d.day}{d.month}{d.year}'.format(d=date)):
        return True, '{d.day}/{d.month}/{d.year}'
    # day - month - year, only month 0 padding
    elif checkIfPalindrome('{d.day}{d.month:02}{d.year}'.format(d=date)):
        return True, '{d.day}/{d.month:02}/{d.year}'
    # day - month - year, both 0 padding
    elif checkIfPalindrome('{d.day:02}{d.month:02}{d.year}'.format(d=date)):
        return True, '{d.day:02}/{d.month:02}/{d.year}'
    
    # month - day - year, no 0 padding
    elif checkIfPalindrome('{d.month}{d.day}{d.year}'.format(d=date)):
        return True, '{d.month}/{d.day}/{d.year}'
    # month - day - year, only day 0 padding
    elif checkIfPalindrome('{d.month}{d.day:02}{d.year}'.format(d=date)):
        return True, '{d.month}/{d.day:02}/{d.year}'
    # month - day - year, both 0 padding
    elif checkIfPalindrome('{d.month:02}{d.day:02}{d.year}'.format(d=date)):
        return True, '{d.month:02}/{d.day:02}/{d.year}'
    else:
        return False, ''


def getNextPalindromeDate(date):
    isPalindrome = False
    while not isPalindrome:
        date += timedelta(days=1)
        isPalindrome, dateformat = checkIfDateIsPalindrome(date)
    return dateformat.format(d=date), dateformat


       
def getNextPalindromeYear(date):
    isPalindrome = False
    while not isPalindrome:
        date += datedelta.YEAR
        isPalindrome, dateformat = checkIfDateIsPalindrome(date)
    return dateformat.format(d=date), dateformat

# Testing

# delta = datetime.datetime.now()
date = datetime.datetime(2022,2,2)
print(date)