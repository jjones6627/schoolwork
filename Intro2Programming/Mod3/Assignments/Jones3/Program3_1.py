#John Jones SPCID: 2515656

#Define constants and variables
#WEEKDAY_OT_RATE = 1.5 if >40
#WEEKEND_OT_RATE = 2.0
#hourly_rate = input from user ($xx.xx)
#weekday_hours = input from user (xx.x)
#weekend_hours = input from user (xx.x)
#regular_pay = hourly_rate * weekday_hours if <= 40
#ot_pay = (hourly_rate * WEEKDAY_OT_RATE) * (weekday_hours - 40)
#weekend_pay = (hourly_rate * WEEKEND_OT_RATE) * weekend_hours
#Output (print) for the week:
#regular_pay
#ot_pay
#weekend_pay
#total_pay = regular_pay + ot_pay + weekend_pay

def main():
    #Define variables
    WEEKDAY_OT_RATE = 1.5    
    WEEKEND_OT_RATE = 2.0
      
    #User Input
    hourly_rate = float(input('Please enter your hourly rate of pay: '))
    weekday_hours = float(input('Please enter the number of weekday hours worked: '))
    weekend_hours = float(input('Please enter the number of weekend hours worked: '))

    #Process pay types
    regular_pay = weekday_hours * hourly_rate  
    if weekday_hours > 40.0:
       ot_pay = (weekday_hours - 40) * (hourly_rate * WEEKDAY_OT_RATE)
    weekend_pay = weekend_hours * (hourly_rate * WEEKEND_OT_RATE) 
    total_pay = regular_pay + ot_pay + weekend_pay
                          
    #Output
    print(f'Regular Pay: ${regular_pay:,.2f}')
    print(f'Overtime Pay: ${ot_pay:,.2f}')
    print(f'Weekend Pay: ${weekend_pay:,.2f}')
    print(f'Total Pay: ${total_pay:,.2f}')

main()

#Collaboration: I worked alone
