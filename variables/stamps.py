# Define a procedure, stamps, which takes as its input a positive integer in pence and returns the number of 5p, 2p and 1p stamps (p is pence) required to make up that value. The return value should be a tuple of three numbers (that is, your return statement should be followed by the number of 5p, the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as needed to make up the total.
#

def stamps(n):
    p5=n/5
    r5=n%5
    p2=r5/2
    p1=r5%2
    return p5,p2,p1
