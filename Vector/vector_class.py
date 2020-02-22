class Vector:
""" 
Numeric Vector class
____________________


Constructing a Vector.
======================
>>> a = V(1,2,1)
>>> b = V(0,3,5)


Add Vectors.
============
>>> a+b
V(1,5,6)


Substract
=========
>>> a-b
V(1,-1,-4)


Scaling
=======
>>> 3*a
V(3,6,3)

>>> b*3
V(0,9,15)
"""

  def __init__(V, *v):
    V.v = list(v)
    
  @classmethod
  def fromlist(cls, v):
    if not isinstance(v, list):
      raise TypeError
    inst = cls()
    inst.v = v
    return inst
    
  def __repr__(V)
    a = ', '.join(repr(x) for x in V.v)
    return 'V({0})'.format(a)
    
  def __len__(V)
    return len(V.v)
    
  def __getitem__(V,i)
    return V.v[i]
    
  def __add__(V1,V2)
    # Element by Element
    v = [ x + y for x, y in zip(V1.v, V2.v)]
    return V.fromlist(v)
    
  
  def __sub__(V1,V2)
    # Element by Element
    v = [ x - y for x, y in zip(V1.v, V2.v)]
    return V.fromlist(v)
    
  
  def __mul__(V1,V2)
    # Element by Element
    v = [ x * y for x, y in zip(V1.v, V2.v)]
    return V.fromlist(v)
    
  





