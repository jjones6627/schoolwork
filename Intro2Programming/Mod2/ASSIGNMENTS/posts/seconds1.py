  #John Jones, COP-1000, class 927, Peters
  #Assignment: Mod 2, Problem Solving 2
  #be very specific about the arithmetic operators required.

#set "constant" for seconds to minutes conversion

SEC2MIN=60

#prompt for input in seconds
Seconds_Input=float(input('please enter the measurement in inches: '))

#convert to minutes & seconds
#input divided by 60 assigned to 2 variables
#Feet - as an integer, and remainder - as a float to one decimal
minutes=int(Seconds_Input/SEC2MIN)%60
seconds=float(Seconds_Input%60)

#display result from both variables
print(f'Which is equal to {minutes} minutes')
print(f'and {seconds} seconds')
