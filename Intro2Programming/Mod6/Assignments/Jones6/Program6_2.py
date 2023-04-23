#John Jones SPCID#2515656
#Collaboration: I worked alone.

#open flight_specials.txt as read and assign to file object flight_specials
#set variable destination as flight_specials.readline()
#Create variables for each header title to allow alignmemnt
#create headers using an f' string to establish columns
#start while loop, testing for a blank value for destination
#Read values for regular_price and reduction_percent
#strip \n from all values

#set value of reduced to float(regular_price) * (float(reduction_percent)/ 100)
#set value of sale_price to float(regular_price) - reduced 
#create an f string print statement using destination, regular_price, reduction in price and sale price
#inside loop continuance:destination = flight_specials.readline() 
#close the flight_specials

def main ():

    flight_specials = open('flight_specials.txt', 'r')

    destination = flight_specials.readline()

    h1 = 'DESTINATION'
    h2 = 'REG. PRICE'
    h3 = 'REDUCED'
    h4 = 'SALE PRICE'

    print(f'{h1:<16}{h2:>9}{h3:>10}{h4:>12}')
    
    while destination != '':

        regular_price = flight_specials.readline()
        reduction_percent = flight_specials.readline()
        
        destination = destination.rstrip('\n')
        regular_price = float(regular_price.rstrip('\n'))
        reduction_percent = reduction_percent.rstrip('\n')

        reduced = float(regular_price) * (float(reduction_percent)/ 100)
        sale_price = float(regular_price) - reduced

        print(f'{destination:<16}{regular_price:>10.2f}{reduced:>10.2f}{sale_price:>12.2f}')

        destination = flight_specials.readline()        
        
    flight_specials.close()    
         
if __name__ == '__main__':    

    main()

