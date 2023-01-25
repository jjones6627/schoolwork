#John Jones  SPCID: 2515656

#Establish constant for user maximum spend of fifty dollars, as an integer (MAX_SPEND) 
#Request user input in whole dollars (no cents) <= $50 and assign to variable (cost) as integer
#determine number of each bill given as change by...
#dividing (change) by 20 assigned to (twenty), find the (leftover) change%20, re-assign value of (change) to (leftover)
#dividing (change) by 10 assigned to (ten), find the (leftover) change%10, re-assign value of (change) to (leftover)
#dividing (change) by 5 assigned to (five), find the (leftover) change%5, re-assign value of (change) to (leftover)
#dividing (change) by 1 assigned to (one)
#Output change in number of each bill given from largest bill to smallest as shown:
  #Bills dispensed as change:
  #$20 - X
  #$10 - X
  #$5 - X
  #$1 - X

def main():

  #Set constants
  MAX_SPEND=50

  #Input
  cost=int(input('Please enter the cost in whole dollars, <= $50:'))

  #Process
  change=MAX_SPEND-cost
  twenty=change//20
  leftover=change%20
  change=leftover
  ten=change//10
  leftover=change%10
  change=leftover
  five=change//5
  leftover=change%5
  change=leftover
  one=change//1
  
  #output
  print('')
  print(f'Bills dispensed as change:')
  print(f'$20 - {twenty}')
  print(f'$10 - {ten}')
  print(f'$5 - {five}')
  print(f'$1 - {one}')
  
main()
