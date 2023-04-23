#John Jones SPCID#2515656
#Collaboration: I worked alone.

#module_5_1 (external module file)

#Define the subtotal_per_item function with parameters of:
 #item description (des), irtem part number (prtnum), item price (price) and quantity ordered (qty)
 #which were passed as arguments in the call.
#code then actual process of calculating the subtotal (price*qty) assigned to variable result
#print the last line (including subtotal) for each item, plus a blank line for separation:
 #f'Item: {des}, Part Number: {prtnum}, subtotal: ${result:,.2f}'
#Return the result to the main function of the calling program for total of purchase accumulation


def subtotal_per_item(des, prtnum, price, qty):
    
    result = price*qty
    
    print(f'Item: {des}, Part Number: {prtnum}, subtotal: ${result:,.2f}')
    print()    

    return result       
    





