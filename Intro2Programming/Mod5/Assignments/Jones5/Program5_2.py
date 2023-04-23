#John Jones SPCID#2515656
#Collaboration: I worked alone.

#Import the math module
#Define main function:
    #Request the radius from user assigned as a float to the variable radius
    #call the area function passing the radius as an argument.
    #area = 4 * math.pi * rad**2
    #Assign return to variable surface_area
    #output the surface area of a sphere with the defined radius to 4 decimals
    #call the volume function passing the radius as an argument
#volume function: volume = 4/3 * math.pi * rad**3 
#print the result from the function

import math

def main ():
    radius = float(input('Enter radius of sphere '))

    surface_area = area(radius)
    
    print(f'The surface area of a sphere with a radius of {radius} is {surface_area:,.4f}')

    volume(radius)          

def area(rad):
    area = 4 * math.pi * rad**2
    return area
    
def volume(rad):
    volume = 4/3 * math.pi * rad**3 
    print(f'The volume is {volume:,.3f}')

if __name__ == '__main__':

    main()


