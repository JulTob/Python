##  Python Test Script File
####  Run by writting "python test.py" in the terminal from path
##  Calculates pi from random points in a 1x1 plane

from random import *
pi_r = 0
pi_p = 0
much = 1500
for x_way in range(1,much):
    x = random() 
    y = random()
    if (x**2 + y**2) <= 1:
        pi_p = pi_p +1
pi_r = 4* pi_p / much
print(pi_r)
