def bigger(x,y):
	result = x
	if x<y:
		result = y
	return result

def biggest(x,y,z):
	return bigger(bigger(x,y),z)

# Well, is actually in the main library. 
def biggest2(x,y,z):
	return max(x,y,z)



def median (x,y,z):
    a=biggest (x,y,z)
    b=bigger (x,y)
    c=bigger (z,y)
    d=bigger (z,x)

    if x==a:
        result= c
    if y==a:
        result= d
    if z==a:
        result= b

    return result

