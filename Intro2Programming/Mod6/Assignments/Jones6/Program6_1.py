#John Jones SPCID#2515656
#Collaboration: I worked alone.

#open flight_specials.txt as write and assign to flight_specials
#Get user input for destination or Enter to quit and assign to destination (primer)
#start while loop: while destination != '':

#Get user input for regular price as variable reg_pr
#get user input for reductions as a percent as reduction_pct

#write statements into flight_specials (one per line) as:
#destination + '\n' and reg_pr + '\n' and reduction_pct + '\n'
#continue loop by getting the next destination in order to check for '' value
#if user presses enter, close flight_specials and print 'file was created'

def main ():

    flight_specials = open('flight_specials.txt', 'w')

    destination = input('Enter destination name or Enter to quit ')
        
    while destination != '':
        
        reg_pr = input('Enter flight\'s regular price ')
        reduction_pct = input('Enter reduction percent for sale ')
        
        flight_specials.write(destination + '\n')
        flight_specials.write(reg_pr + '\n')
        flight_specials.write(reduction_pct + '\n')
        
        destination = input('Enter destination name or Enter to quit ')

    flight_specials.close()

    print('File was created')


if __name__ == '__main__':    

    main()

