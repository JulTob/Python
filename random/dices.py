import rando

def roll(sides = 6)
  num = random.randint(1,sides)
  return num
  
  
def main():
	sides = 6
	rolling = True
	while rolling:
		again = input("Roll again? Y/N")
		if again.lower() != "n":
			num = roll(sides)
			print(num)
		else:
			rolling = False
	print("Bye!")
