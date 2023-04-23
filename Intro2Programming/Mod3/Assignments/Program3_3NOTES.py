#John Jones SPCID: 2515656

#Define constants and variables
#

#Get user input
#integerA = int(input('Enter the first number ==>  '))
#integerB = int(input('Enter the second number ==>  '))
#integerC = int(input('Enter the third number ==>  '))

#if integerA < integerB:
#   if integerA < integerC:
#       smallest = integerA
#   else:
#       smallest = integerC
#else:
#   if integerB < integerC:
#       smallest = integerB
#   else:
#       smallest = integerC   
#
    #ALTERNATIVE?
    #Process to determine which is smallest
    #if integerB < smallest:
    #   if integerC < integerB:
    #       then: smallest = integerC
    #   else:
    #       smallest = integerB
    
#Output
#print (smallest)

def main():
    #Define constants and variables
    #none
    #Get user input
    integerA = int(input('Enter the first number ==>  '))
    integerB = int(input('Enter the second number ==>  '))
    integerC = int(input('Enter the third number ==>  '))


    #Process to determine which is smallest
    if integerA < integerB:
       if integerA < integerC:
           smallest = integerA
       else:
           smallest = integerC
    else:
       if integerB < integerC:
           smallest = integerB
       else:
           smallest = integerC
           
    #Output
    print (smallest)
    


main()
#Collaboration: I worked alone.

#Write a program that prompts the user to enter three integers one at a time.
#The program should determine which integer is smallest and print the result
#Use nested decision blocks and pay close attention to proper indentation.
