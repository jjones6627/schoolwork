#John Jones  SPCID: 2515656

#Establish constant for user maximum spend of fifty dollars, as an integer (MAX_SPEND) 
#Request user input in whole dollars (no cents) <= $50 and assign to variable (cost) as integer
#Using subtraction (-), multiplication (*), division of integer (/) and modulus (%) operators,
#determine variables for bills given as change
#create variable for MAX_SPEND-cost for ease of processing
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
  ten=change%20//10
  five=(change-(twenty*20)-(ten*10))//5
  one=(change-(twenty*20)-(ten*10)-(five*5))//1

  #output
  print('')
  print(f'Bills dispensed as change:')
  print(f'$20 - {twenty}')
  print(f'$10 - {ten}')
  print(f'$5 - {five}')
  print(f'$1 - {one}')
  
main()
