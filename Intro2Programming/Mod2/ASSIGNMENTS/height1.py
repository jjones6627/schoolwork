  #John Jones, COP-1000, class 927, Peters
  #Assignment: Mod 2, Problem Solving 1

#set "constants" for inch to cm and ft to inch conversions
INCH_CM_RATIO=2.54
FT_INCH_RATIO=12

#get height in feet and inches (two variables)and convert both to integers
feet=int(input("please enter your height in feet: "))
inches=int(input("and inches: "))
    
#convert feet var to inches and get total inches
total_inch=FT_INCH_RATIO*feet+inches
    
#convert inches to centimeters (X 2.54)
totalCM=total_inch*INCH_CM_RATIO
    
#display result
print(f'your height in centimeters is: {totalCM}')
      
