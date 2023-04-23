#John Jones SPCID#2515656
#Collaboration: I worked alone.

#set a variable, string, to contain each iteration output
#create outer loop to run the inner loop three times
#create the inner loop that runs 9 times to build and output the string for each line.
#convert the integer in the range to a string,
#concatenate the next integer, as a string, to the former value of string
#print string
#reset value of string for each of 3 runs

def main ():

    for num in range(1,4):
        string=('')
        for character in range(0,10):            
            string=string + str(character)
            print(f'{string}')
            
main()
