#John Jones SPCID: 2515656

#Define constants and variables
#BASE_CHARGE = 500
#CHARGE_3_ACC = 600
#CHARGE_2_ACC = 400
#CHARGE_1_ACC = 200
#AGE_FEE = 100
#acc_charge = 0
#age_charge = 0

#Input from user:
#driver_age
#driver_accidents

#if driver_accidents = 3:
#   acc_charge = CHARGE_3_ACC
#elif driver_accidents = 2:
#   acc_charge = CHARGE_2_ACC#
#elif driver_accidents = 1:
#   acc_charge = CHARGE_1_ACC#
#else: acc_charge = 0.00

#if driver_age <25:
#   age_charge = AGE_FEE

#Insurability boolean: if driver_age <25 AND driver_accidents >2 = True: deny
#Insurability boolean: driver_accidents >3 = True: deny
#If False:
#Output: policy_amount = BASE_CHARGE + acc_charge + age_charge

def main():
    #Define variables
    BASE_CHARGE = 500
    CHARGE_3_ACC = 600
    CHARGE_2_ACC = 400
    CHARGE_1_ACC = 200
    AGE_FEE = 100
    acc_charge = 0
    age_charge = 0

    #Input from user:
    driver_age = int(input('Enter age of insured: '))
    driver_accidents = int(input('Enter the number of accidents: '))
    
    #Process insurable
    if driver_accidents == 3:
       acc_charge = CHARGE_3_ACC
    elif driver_accidents == 2:
       acc_charge = CHARGE_2_ACC
    elif driver_accidents == 1:
       acc_charge = CHARGE_1_ACC
    else: acc_charge = 0

    if driver_age <25:
       age_charge = AGE_FEE
    
    #Process insurability
    if driver_accidents >3:
        print(f'You are uninsurable at this time')
    else:        
        if driver_age <25 and driver_accidents >2:
            print(f'You are uninsurable at this time')
        else: #Output:   
            policy_amount = BASE_CHARGE + acc_charge + age_charge
            print('')
            print(f'Policy Amount: ${policy_amount:,}')
 
main()
#Collaboration: I worked alone.
