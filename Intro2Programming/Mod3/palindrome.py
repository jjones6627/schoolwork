#John Jones CL-1000 927
#Palindrome date checker
#Collaboration: I worked alone in class
#
def main():
    print(f'{"Palindrome Date":<15}')
    print('---------------')
    for year in range (0,100):
        leap_yr = False
        if year%4 == 0:
            leap_yr == True
        for month in range (1,13):
            if  month == 1:
                last_day = 31
            elif month == 2:
                if leap_yr:
                    last_day = 29
                else:
                    last_day = 28
            elif month == 3:
                last_day = 31
            elif month == 4:
                last_day = 30
            elif month == 5:
                last_day = 31
            elif month == 6:
                last_day = 30
            elif month == 7:
                last_day = 31
            elif month == 8:
                last_day = 31                
            elif month == 9:
                last_day = 30
            elif month == 10:
                last_day = 31
            elif month == 11:
                last_day = 30
            elif month == 12:
                last_day = 31
            for day in range (1, last_day+1):
                if year > 9:
                    if day > 9:
                        date = month * 10000 + day * 100 + year
                    else:
                        date = month * 1000 + day * 100 + year
                else:
                    if day > 9:
                        date = month * 1000 + day * 10 + year
                    else:
                        date = month * 100 + day * 10 + year
                        
                number = date
                temp = number
                reverse_num = 0
                while (number > 0):
                    digit = number%10
                    reverse_num = reverse_num * 10 + digit
                    number = number // 10
                if (temp == reverse_num):
                    print(f'{month}/{day}/{year}')
                    
if __name__=='__main__':
    main()
                
                
