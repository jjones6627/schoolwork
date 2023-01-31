#John Jones  SPCID: 2515656

#Establish a constant for the ratio of feet to fathom (FT_TO_FATHOM = 0.166667)
#Prompt the user to "enter the number of feet to nearest 10th", assign as a float to one decimal to variable (feet)
#Multiply (feet) * (FT_TO_FATHOM), assign to new variable (fathoms)
#Display the original number of (feet) and the value of (fathoms), accurate to 3 decimals, to the user 

def main():
  #Set constants
  FT_TO_FATHOM = .166667  #One foot is equal to .166667 fathoms

  #Input
  feet=float(input("Please enter the number of feet to the nearest 10th:"))

  #Process
  fathoms=(feet*FT_TO_FATHOM)

  #Output
  print(f'{feet} feet are equal to {fathoms:,.3f} fathoms')

main()  

