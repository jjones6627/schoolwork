# quad_compre.py

'''
    A list comprehension that solves a quadratic equation
'''

import math as ma

def main():

    print('Enter a, b, c of the equation. Press Enter after each number')
    a = int(input())
    b = int(input())
    c = int(input())

    if 4*a*c > b**2:
        print('There is no solution with those values')
    else:
        r1,r2 = [(-b + ma.sqrt(b**2 - 4*a*c))/2/a,(-b - ma.sqrt(b**2 - 4*a*c))/2/a]
        print(f'The roots are {r1} and {r2}')

if __name__ == '__main__':
    main()

    
    
