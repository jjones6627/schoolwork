#John Jones  SPCID: 2515656

#Set constants for base price ($24.99), shipping & handling per widget ($1.00), and tax rate (7%)
#Ask user to input the number of widgets wanted, save as variable (order)
#Multiply (WIDGET_BASE_COST) * (order) and assign to variable (widget_cost)
#Multiply (S_H_PER_WIDGET) *(order) and assign to variable (s_h_total)
#Multiply (TAX_RATE) * (widget_cost) and assign to variable (tax_total)
#Add(widget_cost) + (s_h_total) + (tax_total) and assign to variable (total)
#Output to user with detailed receipt as shown in Customer Requirements: program2_3

def main():
    #Constants
    WIDGET_BASE_COST=24.99
    S_H_PER_WIDGET=1.00
    TAX_RATE=0.07

    #Input
    order=int(input('How many Widgets do you want? ==>'))

    #Process
    widget_cost=WIDGET_BASE_COST*order
    s_h_total=S_H_PER_WIDGET*order
    tax_total=TAX_RATE*widget_cost
    total=widget_cost+s_h_total+tax_total

    #Output
    print('')
    print('   R E C E I P T')
    print('')
    print(f'Widgets\' base cost : ${float(widget_cost):,.2f} ({order:,} @ ${WIDGET_BASE_COST})')
    print(f'S&H : ${s_h_total:,.2f}')
    print(f'Tax : ${tax_total:,.2f}')
    print('')
    print(f'Total : ${total:,.2f}')
  
main()



