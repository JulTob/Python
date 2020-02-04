'''
solves equations of the style
  ax² + bx + c = 0
  Julio Toboso
'''
import numpy as np
import cmath as cm
from numpy import sqrt

def solvequadratic(a,b,c):
    a , b, c = float(a), float(b), float(c)
    if c == 0 :
      return 0,-b
    c = ((b ** 2.0) - 4.0 * a * c)
    if c<0: s = 1j * cm.sqrt(-c)
    else: s = np.sqrt(c)
    return (-b+s)/(2*a) , (-b-s)/(2*a)


print(
    np.around(
        solvequadratic(-2,2,-3),
        3)
    )
