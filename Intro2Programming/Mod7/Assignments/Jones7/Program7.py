#John Jones SPCID#2515656
#Collaboration: I worked alone.

#define variables count, accum, minor & senior
#use a list comprehension to generate 100 random integers all from 1 to 100, inclusive.
#pass the list as the sole argument to the custom value-returning function.

    #sort the list in descending order using methods sort and reverse
    #return the sorted list to main

#within a for loop to print a 10 by 10 representation of the ages returned by the custom function.
#As listed in the example output, the ages should be in descending order and evenly spaced.
#Also, within the same for loop accumulate the sum of all ages.

#using a built-in function max to determine the age of the oldest person, then print it
#using a built-in function min to determine the age of the youngest person, then print it 
#determine the average age by making use of the sum of all ages calculated in the for loop above and a built-in function len 
#then print the average age so that two decimal positions are included

#within a for loop: count the minor ages that are less than 18 & count the senior ages that are greater than 65
#print the count of minor ages & print the count of senior ages 
#use a list comprehension to create a list of college ages (ages that are greater or equal to 18 and less than or equal to 21).
#print the count of college-age adults making use of a built-in function len

import random

def main():

    count = 1
    accum = 0
    minor = 0
    senior = 0

    initial_list = [random.randint(1, 100) for number in range(100)]
    sorted_list = custom_function(initial_list)
    
    for num in sorted_list:
        if count%10 == 0:
            print(f'{num:>3}')
        else:
            print(f'{num:>3}', end=' ')
        if num < 18:
            minor += 1
        if num > 65:
            senior += 1
        accum += num        
        count += 1
        
    print(f'Oldest person: {max(sorted_list)}')
    print(f'Youngest person: {min(sorted_list)}')
    print(f'Average age: {accum/len(sorted_list):.2f}')
    print(f'Number of minors is: {minor}')
    print(f'Number of seniors is: {senior}')

    college_list = [item for item in sorted_list if item >=18 and item <= 21]
    print(f'There were {len(college_list)} college-age adults in the survey')


def custom_function(inlist):
    inlist.sort()
    inlist.reverse()
    return inlist
    

if __name__ == '__main__':    

    main()

