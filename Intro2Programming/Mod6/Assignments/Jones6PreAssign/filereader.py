#John Jones COP-1000  #927
#Collaboration: I worked alone.

#Mod 6 pre-assignment 2

#open friends.txt as read and assign to friends_file
#set variable line as friends_file.readline()
#Initialize variables: line_num = 1, accum = 0, age_count = 0
#start while loop testing for a blank line: while line != '':
#utilize if-else to select the odd lines for names and the even lines for ages
#strip \n fromm name and age values
#advance variables from age lines for next iteration: accum, age_count
#at the end of each age (even) line print the statement containing both values
#Outside of the if-else, advance the variables that occur every iteration: line_num
#restart cycle :line = friends_file.readline()
#close the friends_file
#set variable average_age to = accum / age count
#print the average age of your friends to one decimal.

def main ():

    friends_file = open('friends.txt', 'r')

    line = friends_file.readline()
    
    line_num = 1
    accum = 0
    age_count = 0
        
    while line != '':

        if line_num % 2 != 0:
            name = line.rstrip('\n')
             
        else: 
            age = line.rstrip('\n')
            accum = accum + int(age)
            age_count = age_count+1
            print(f'My friend {name} is {age}')

        line_num = line_num+1
        
        line = friends_file.readline()    
        
    friends_file.close()

    average_age = accum / age_count

    print(f'Average age of friends is {average_age:.1f}')

        
if __name__ == '__main__':    

    main()

