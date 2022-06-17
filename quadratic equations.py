##############
#name:Cynthia
#age:17
#gender:female
##########

import math
a=int(input('Enter the co-efficient of the first term'))
b=int(input('Enter the co-efficient of the second term'))
c=int(input('Enter the constant'))
w=math.sqrt((b**2)-4*a*c)

def find_roots(a,b,c):
    y_1 =(-b + w/(2*a))
    y_2 =(-b - w/(2*a))
print("the roots of the quadratic equations are:",find_roots)    