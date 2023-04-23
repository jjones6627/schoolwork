#John Jones SPCID#2515656
#Collaboration: I worked alone.

#Import Program5_2
#Define main function:
#Get radius from user as a float, assigned to variable radius
#Call Program5_2.area passing radius as an argument and assigmning return as variable surface_area
#Print the result to 4 decimal places
#Call Program5_2.volume passing radius as an argument which will calculate and print its result

import Program5_2

def main ():
    
    radius = float(input('Enter radius of sphere '))

    surface_area = Program5_2.area(radius)
    
    print(f'The surface area of a sphere with a radius of {radius} is {surface_area:,.4f}')

    Program5_2.volume(radius) 


if __name__ == '__main__':

    main()

