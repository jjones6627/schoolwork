#John Jones COP-1000 # 927
#Collaboration: I worked alone.

    #I could not find how to associate the temps.py module to this 5_2 preassignment.
    #I was not able to test this program.  Let me know what I'm missing.

#Import the module temps in order to use the 2 functions required.
#define the main function:
#Get user input as an integer "Enter a temperature", save as variable temp
#Ask user if temp was in Celsius of Fahernheit, save as variable c_f
#If c_f is Celsius (C), call c_to_f function to convert to Fahernheit (F)
#Print the result as temp Celsius equals temp Fahrenheit to two decimal places
#If c_f is Fahernheit (F), call f_to_c function to convert to Celsius (C)
#Pass the value back to the main function and print the result
#as temp Fahrenheit equals temp Celsius to two decimal places


import Temps

def main ():
    temp = int(input('Enter a temperature: '))
    c_f = input('Was that input Fahrenheit or Celsius? c/f: ')        
    
    if c_f == 'c':
        Temps.c_to_f(temp)
        

    else:
        cel_temp = Temps.f_to_c(temp)
        print(f'{temp} Fahrenheit equals {cel_temp:.2f}')


if __name__ == '__main__':

    main()


