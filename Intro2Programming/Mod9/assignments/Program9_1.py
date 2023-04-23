#John Jones SPCID#2515656
#Collaboration: I worked alone.

 #the program will store current grades in a dictionary using course codes as keys
 #and with values consisting of percent grades in lists.
 #The main functions of this program are to print a student's gradebook, to drop the lowest grade in each course,
 #print the student's gradebook again, drop the course with lowest average, and finally printing the student's gradebook again. 
 #This program requires a main function and a custom value-returning function.

 #In the main function:
 #code these basic steps in this sequence (intermediate steps may be missing):
 #start with an empty dictionary that represents a gradebook
 #use a while loop to allow the input of course codes from the keyboard.
 #End the while loop when the user presses enter without entering data.

 #within the while loop:
 #for each course entered, use a list comprehension to generate five random integers in the range of 70 through 100.
 #These random integers in a list represent the grades for the course. 
 #after entering the courses, call a custom function passing to it the dictionary now populated with course information and associated grade information

 #In the custom function:
 #print the underlined headings for Course, Average Grade and Grades columns.
 #See the example output for proper formatting
 #(hint: use an 8-character width, left justified for "Course"; use 5-character width, centered, for "Avg"; and use 25-character width for "Grades")
 #use a for loop and the items method to extract the course and grade data from gradebook.

 #within the for loop:
 #use a built-in method to sort the list of grades
 #use another for loop to sum all grades for the course
 #calculate the average for the course using the sum of all grades and a built-in function to determine the number of grades in the list of grades

 #use an if statement to determine the course with the lowest average
 #(hint: this may require initializing the variable used to store the lowest average to the highest possible grade value prior to the for loop). 
 #print the course and its average.

 #Use format identifiers to allow for printing of a left-justified course with a width of 8 and for an average with a width of 4 including 1 decimal place.
 #use another for loop to print all grades in the grades list for the course.
 #Use a format identifier to allow for printing of a right-justified grade with a width of 4 followed by a percent sign.

 #calculate and print the term average using the previously calculated sum of all grades and built-in functions
 #to determine the number items in the gradebook dictionary and grade list.

 #Use a format identifier to allow for printing of a grade with a width of 4 including one decimal position followed by a percent sign.
 #return the course with the lowest average

  #Back in main function:
  #print a message indicating that the lowest grades are being dropped.  See the example output for proper formatting.
  #use a for loop and the values method of the gradebook to extract the grades list for each course
  #within the for loop:
  #use a built-in function to determine the lowest grade from the grades list for a particular course
  #use a built-in function to remove the lowest grade
  #print a message indicating that courses and grades are being printed after the lowest grades have been dropped.  See the example output for proper formatting.

  #call the custom function again passing to it the updated dictionary now populated with course information and associated grade information
  #with the lowest grades for each course dropped
  #drop the lowest course, which is returned by the custom function, from the gradebook. Use a built-in function to drop the course.
  #print a message indicating that courses and grades are being printed after the lowest course has been dropped.  See the example output for proper formatting.
#call the custom function again passing to it the updated dictionary now populated with course information and associated grade information with the lowest course dropped
#For your testing purposes, enter at least five courses although any amount should be allowed to be entered

import random
def main():

    gradebook = {}

    course_code = input('Enter a course code or Enter to quit:  ')
                 
    while course_code != '':
        grades = [random.randint(70,100)for int in range(5)]
        gradebook[course_code] = grades
        course_code = input('Enter a course code or Enter to quit:  ')
    lowest_class = print_func(gradebook)
    print('Dropping the lowest grades...')
    for grades in gradebook.values():
        lowest_grade = min(grades)
        grades.remove(lowest_grade)
    print('Here are the courses and grades after dropping the lowest grades:')
    lowest_class = print_func(gradebook)
    del gradebook[lowest_class]
    print(f'Dropping the lowest course:{lowest_class}')
    print('Here are the courses and grades after dropping the lowest course:')
    print_func(gradebook)
      
    

def print_func(gradebook):
    print()
    print(f'Here are the courses and grades:')
    print()
    print(f'{"Course":<8} {"Avg":^5} {"Grades":^25}')
    print(f'{"------":<8} {"---":^5} {"-----------------------":^25}')
    for key, value in gradebook.items():
        value.sort()
        
        ttl = 0
        count = 1
        oa_avg = 0
        low_avg = 100
        low_class = ''
        
        for grade in value:
            ttl += grade
        avg = ttl/len(value)
        
        if avg < low_avg:
            low_avg = avg
            low_class = key
        
        print(f'{key:<8} {avg:^4.1f}%', end='')
        for grade in value:
            if count%len(value) == 0:
                print(f'{grade:>4}%')
            else:
                print(f'{grade:>4}%', end='')
            count += 1

    oa_avg = oa_avg + avg
    print()
    print(f'Term average is {oa_avg:.1f}%')
    return low_class
    
 
if __name__ == '__main__':    

    main()    
