#John Jones COP-1000 class 927, Mod2 Pre-assignment

#INPUT - get test scores from user, creating 3 float variables: test1, test2, test3
test1=float(input("Please enter the score for test 1: "))
test2=float(input("Please enter the score for test 2: "))
test3=float(input("Please enter the score for test 3: "))

#Find sum (+)of input variables, divide (/) by 3, store as var: avg_score
avg_score=(test1+test2+test3)/3

#PRINT f' string for avg_score to two decimals ending in % sign
print(f'The average of these scores is {avg_score:,.2f}%')
