#John Jones COP-1000 # 927
#Collaboration: I worked alone.

#Import the random module
#Using random.randint, generate a random integer between 1 and 5 inclusive
#repeat twice, saving the outcomes as variables num1 and num2
#Call the show_larger function, passing the 2 variables as arguments
#Define the show_larger function with an if, elif, else statement:
#If int1 > int2, print that statement as well as by how much (int1 - int2)
#Else if they are the same, print The integers are equal, both are {int1}
#Else:(int2 > int1),print that statement as well as by how much (int2 - int1) 


import random

def main ():
    num1 = random.randint(1, 5)
    num2 = random.randint(1, 5)
    show_larger(num1, num2)   


def show_larger (int1, int2):
    if int1 > int2:
        print(f'{int1} is greater than {int2} by {int1 - int2}')
    elif int1 == int2:
        print(f'The integers are equal, both are {int1}')
    else:
        print(f'{int2} is greater than {int1} by {int2 - int1}')



if __name__ == '__main__':

    main()


