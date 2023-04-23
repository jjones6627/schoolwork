#John Jones SPCID#2515656
#Collaboration: I worked alone.

#using a for loop with a range, establish variable num from 100 to 200 in whole numbers.
#if num%5==0 and num%3==0, print (num) and World Cup! as directed
#else if num%5==0, print(num) and World
#else if num%3==0, print (num) and Cup

def main ():

    for num in range(100,201,1):
        if num%5==0 and num%3==0:
            print(f'{num} World Cup!')
        elif num%5==0:
            print(f'{num} World')
        elif num%3==0:
            print(f'{num} cup')
            
main()


