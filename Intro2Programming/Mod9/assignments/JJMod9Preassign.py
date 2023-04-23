#John Jones COP-1000  #927
#Collaboration: I worked alone.

#Mod 9 pre-assignment

 #This assignment requires a dictionary of state abbreviations and their capital cities.
 #The abbreviations are the keys and the state capitals are the values.

 #Start by entering data for any four states of your choice.
 #Then, report this count but use a function to get the count. 
 #Use a while loop to add more abbreviations and capitals.
 #The loop should continue until the user presses
 #Enter when prompted for an abbreviation.

        #while in loop:
        #If the state entered is already in the dictionary, report its capital.
        #If it is not in the dictionary, prompt the user to enter the capital for that state and add it to the dictionary

 #Report again the count of the number of states in the dictionary.
 #Using another loop and the items() method, display all the state abbreviations and their capitals.

 #In the same Python program write this code, although it has nothing to do with the states code.
#Using a dictionary comprehension, create a dictionary with the odd integers from 1 to 9 as keys and their cubes as values.
#Use a for loop to display the keys and values but without using the items() method.

def main():

    capitals = {'IA':'Des Moines', 'OH':'Columbus', 'FL':'Tallahasee', 'IN':'Indianapolis'}
    
    num_items = len(capitals)
    
    print(f'{num_items} states are in the dictionary')
    print(f'Let\'s add a few more')

    abbrev = str(input('Enter state abbrev. or Enter to quit:  '))
                 
    while abbrev != '':
                      
        if abbrev in capitals:
            print(f'Already have {abbrev}, capital is {capitals[abbrev]}')
        else:
            capital = input('Enter capital of ' + abbrev + ':  ')
            capitals[abbrev] = capital
            
        abbrev = input('Enter state abbrev. or Enter to quit:  ')
        
    num_items = len(capitals)
    print()
    print(f'Got {num_items} states now. Here they are...')

    for key, value in capitals.items():
        print(f'The capital of {key} is {value}')

###############################################################        

    oddz_N_cubez = {item:item**3 for item in range(1,10,2)}
        
    print()
    print('Some cubes made with a dictionary comprehension...')
    for key, value in oddz_N_cubez.items():
        print(f'{key} cubed is {value}')


if __name__ == '__main__':    

    main()
