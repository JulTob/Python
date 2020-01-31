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
