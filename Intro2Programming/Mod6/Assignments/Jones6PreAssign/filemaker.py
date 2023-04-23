#John Jones COP-1000  #927
#Collaboration: I worked alone.

#Mod 6 pre-assignment 1

#open friends.txt as write and assign to friends_file
#Get user input for name or Enter to quit
#start while loop: while name != '':
#Get user input for age as variable age
#write statements into friends_file as name + '\n' and age + '\n'
#re-start loop by getting the next name in order tom check for ''
#if user presses enter, close friends_file and print 'file was created'

def main ():

    friends_file = open('friends.txt', 'w')

    name = input('Enter the first name of friend or Enter to quit ')
        
    while name != '':
        
        age = input('Enter age (integer) of this friend')

        friends_file.write(name + '\n')
        friends_file.write(age + '\n')
        
        name = input('Enter the first name of friend or Enter to quit ')

    friends_file.close()

    print('File was created')

        
if __name__ == '__main__':    

    main()

