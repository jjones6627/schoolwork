#John Jones SPCID#2515656
#Collaboration: I worked alone.

#Import the external module_5_1
#define main function
#Prompt user for number of products being ordered (as num_of_prods) to populate loop range
#establish variables item_num = 1 and total = 0.00
#set up for-loop to run the number of times as there are products ordered
#For each loop iteration:
    #prompt user for item description, part number, cost and quantity
    #call the external function, with above as arguments, to calculate & print subtotal per item 
    #change variables for the next loop iteration: total = total + subtotal, item_num = item_num + 1
#When loop ends, print the total of the sale     
#Dunder statement & call main function

import module_5_1

def main ():    

    num_of_prods = int(input('How many different items are being purchased? '))
    print()

    item_num = 1
    total = 0.00

    for number in range(1, num_of_prods + 1):        

        descr = input('Enter description of item '+ str(item_num)+ ' ')
        part_num = input('Enter part number of item '+ str(item_num)+ ' ')
        item_price = float(input('Enter price of item '+ str(item_num)+ ' '))
        item_qty = int(input('Enter the quantity for item '+ str(item_num)+ ' '))
        
        subtotal = module_5_1.subtotal_per_item(descr, part_num, item_price, item_qty)        

        total = total + subtotal       
        item_num = item_num + 1
   
    print(f'Your total is ${total:,.2f}')

if __name__ == '__main__':    

    main()

