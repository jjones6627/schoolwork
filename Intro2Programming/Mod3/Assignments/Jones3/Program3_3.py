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
    print(f'{smallest} is the smallest')
   
main()
#Collaboration: I worked alone.

