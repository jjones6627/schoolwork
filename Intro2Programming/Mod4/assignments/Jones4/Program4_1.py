#John Jones SPCID#2515656
#Collaboration: I worked alone.

#Set variables for accumulation, meal count and difference between budget and accumulated to 0
#Get user input for weekly caloric budget as integer and save as variable budget
#Get user input for first meal calories (as an integer) or enter 0 to quit
#while the meal calorie entry is >0:
#add meal calories to accumulation variable
#add 1 to meal count
#reset meal calories to 0
#request user input for another meal calories or enter 0 to quit, loop cycles
#If meal calorie entry == 0:
#print the number of meals entered for the period
#using a nested if statement, determine if the accumulated calories are at, below or above the budget
#print the results as specified: right on plan, over plan or under plan and by how much

def main ():
    accum = 0
    meals = 0
    diff = 0
    budget = int(input('Enter your weekly caloric budget ==> '))
    meal_calories = int(input('Enter calories for a meal (as an integer) or 0 to quit ==>'))
    while meal_calories > 0:
        accum += meal_calories
        meals += 1
        meal_calories = 0
        meal_calories = int(input('Enter calories for another meal (as an integer) or 0 to quit ==>'))        
    if meal_calories == 0:
        print()
        print('You entered',meals,'meals')
        print()
        if accum > budget:
            diff = accum - budget
            print('You are over plan by', diff)
        elif accum < budget:
            diff = budget - accum
            print('You are under plan by', diff)
        else:
            print('Right on budget!')
main()


