#John Jones COP-1000 class 927 Mod 3 Pre-assignment

#Define Constants and Variables:
#TAX_RATE Sales Tax of 7%
#SHIP_RATE Shipping of $1/lb
#SHIP_THRESHOLD Subtotal >= $150
#TIER_1_RATE <10 lbs = $12.00/lb
#TIER_2_RATE >=10 lbs = $10.00/lb
#TIER_3_RATE >=20 lbs = $8.75/lb
#TIER_4_RATE >=40 lbs = $7.50/lb
#subtotal = 0
#ship_cost = 0

#Prompt user to enter a quantity of one or more pounds and save as integer total_pounds 
#If total_pounds >= 40
#   then subtotal = TIER_4_RATE * total_pounds
#Else If total_pounds >= 20
#   then subtotal = TIER_3_RATE * total_pounds
#Else If total_pounds >= 10.00
#   then subtotal = TIER_2_RATE * total_pounds
#Else:
#   subtotal = TIER_1_RATE * total_pounds

#If subtotal <= 150.00
#   then ship_cost = total_pounds * SHIP_RATE

#total_tax = subtotal * TAX_RATE
#total_order = subtotal + total_tax + ship_cost

#Output
#How many pounds are you ordering? xx 
#Cost of coffee $xx.xx
#7% sales tax $xx.xx
#Shipping fee $xx.xx
#Total payable $xx.xx


def main():
    #Set variables
    TAX_RATE = 0.07
    SHIP_RATE = 1.00
    SHIP_THRESHOLD = 150.00
    TIER_1_RATE = 12.00
    TIER_2_RATE = 10.00
    TIER_3_RATE = 8.75
    TIER_4_RATE = 7.50
    subtotal = 0.00
    ship_cost = 0.00
    total_tax = 0.00
    total_cost = 0.00

    #Input
    total_pounds = int(input('How many pounds are you ordering? '))

    #Process subtotal
    if total_pounds >= 40:
       subtotal = TIER_4_RATE * total_pounds
    elif total_pounds >= 20:
       subtotal = TIER_3_RATE * total_pounds
    elif total_pounds >= 10:
       subtotal = TIER_2_RATE * total_pounds
    else:
       subtotal = TIER_1_RATE * total_pounds
       
    #Process shipping cost
    if subtotal <= SHIP_THRESHOLD:
        ship_cost = total_pounds * SHIP_RATE

    #Process tax
    total_tax = subtotal * TAX_RATE

    #Process total order
    total_cost = subtotal + total_tax + ship_cost

    #Output
    print(f'Cost of coffee: ${subtotal:,.2f}')
    print(f'7% Sales tax: ${total_tax:,.2f}')
    print(f'Shipping fee: ${ship_cost:,.2f}')
    print(f'Total payable: ${total_cost:,.2f}')
    
main()

 
