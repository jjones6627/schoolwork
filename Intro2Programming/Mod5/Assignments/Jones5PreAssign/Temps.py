#John Jones COP-1000 # 927
#Collaboration: I worked alone.

#I could not find how to associate this temps.py module to the 5_2 preassignment.
#I was not able to test this program.  Let me know what I'm missing.

#Module: Temps



def c_to_f(c_temp):
    f_temp = c_temp * 1.8 + 32
    print(f'{c_temp} Celsius equals {f_temp:.2f}')


def f_to_c(f_temp):
    c_temp = (f_temp - 32) / 1.8
    return c_temp



