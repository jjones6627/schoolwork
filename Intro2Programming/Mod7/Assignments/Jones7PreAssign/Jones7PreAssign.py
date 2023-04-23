#John Jones COP-1000  #927
#Collaboration: I worked alone.

#Mod 7 pre-assignment

#Define variables for initial_list, list_string, newlist_string
#create an empty list
#Use for-loop to add 12 random integers, ranging from 50 to 100, to the list
#use second for-loop to iterate over the list and display all elements on one line separated by a single space.
#display the 4th element, the element at index 9, and the smallest element.
#call the change_list function with your list as its sole argument.
    #use a slice to make a new list from the list that was passed into this function.
    #The new list should hold the middle 6 elements of the list that was passed in.
    #use a function to determine the size of the new list. Print the size.
    #sort the new list in ascending order and return the sorted list to main.
#assign the list returned by change_list to a new list.
#use a for-loop to iterate over this returned list and display all elements on one line, separated by a single space.


import random

def main ():
    
    list_string = ''
    newlist_string = ''
    initial_list = []
    
    for number in range(12):
        int = random.randint(50, 100)
        initial_list.append(int)
    
    print(f'Here is the list of random integers...')
    for number in initial_list:
        list_string = list_string + str(number)+' '
        
    print(f'{list_string} ')            
    print(f'The 4th element in the list is {initial_list[3]}')
    print(f'The element at index 9 is {initial_list[9]}')
    print(f'The smallest element in the list is {min(initial_list)}')
    
    new_list = change_list(initial_list)

    for number in new_list:
        newlist_string = newlist_string + str(number)+' '
    print(f'change_list returned this sorted list...')
    print(f'{newlist_string} ')


def change_list (list2change):
    new_list = list2change[3:9]
    print(f'The size of the list is now {len(new_list)}')
    new_list.sort()
    return new_list



if __name__ == '__main__':    

    main()

