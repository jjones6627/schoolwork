#John Jones COP-1000 Ch.4 Prep assignment #2
#Collaboration: I worked alone.

#Get user input as an integher or 0 and save it to variable integer
#Use while loop to test integer is greater than 0
#Test for odd or even: While integer > 0: if integer%2==0 then even, else odd.
#using a separate variable to contain odd/even test reult, print the integer and its odd/even status
#Request next user input (integer or 0)
#If integer, loop back through process
#if 0, print All done which ends the loop

def main():
    
    integer = int(input('Enter an integer or 0 to quit: '))

    while integer > 0:
        if integer % 2 == 0:
            odd_even = 'even'
        else:
            odd_even = 'odd'
        print(f'{integer} is an {odd_even} number')
        
        integer = int(input('Enter an integer or 0 to quit: '))
        
    if integer == 0:
        print('All done!')
        
main()
