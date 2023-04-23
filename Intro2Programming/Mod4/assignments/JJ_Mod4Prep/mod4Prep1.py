#John Jones COP-1000 Ch.4 Prep assignment #1
#Collaboration: I worked alone.

#Print the headers with specified spacing
#Set the Range paramenters: num from 5 to 50(+1) in increments of 5
#Establish variables: squares (as num**2) and cubes (as num**3)
#print output aligned with required spacing

def main():
    print(f'{"INTS":^7}{"SQUARES":>8}{"CUBES":>12}')
    for num in range(5, 51, 5):
        squares=num**2
        cubes=num**3
        print(f'{num:^7,}{squares:>8,}{cubes:>12,}')
    
main()
#I will admit I spent a lot of time searching before I indented the final print statement.LOL
