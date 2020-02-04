 # Calculates de distance between two numbers
 # According to the formula
 #    √[ (Px2-Px1)² + (Py2-Py1)² +(Pz2-Pz1)² ]
 
 import numpy as np
 
 x1, y1, z1 = 23.2, 2.5, 0.0
 x2, y2, z2 = 21.5, 0.0, 11.5

dr = np.sqrt( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 )
