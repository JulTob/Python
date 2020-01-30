import csv

def add_record():
  file = open("Salaries.csv","a")
  name = input("Enter name: ")
  salary = int(input("Enter salary: "))
  newrecord = name + ", " + str(salary) + "\n"
  file.write(str(newrecord))
  file.close()
  
def view_records():
  file = open("Salaries.csv","r")
  for row in file:
    print(row)
  file.close()
	
def delete_record():
	file = open("Salaries.csv","r")
	x = 0
	tmplist = []
	for row in file:
		tmplist.append(row)
	file.close()
	for row in tmplist:
		print(x,row)
		x = x+1
	rowtodelete = int(input("Selecte row for deletion: "))
	del tmplist[rowtodelete]
	file = open("Salaries.csv","w")
	for row in tmplit:
		file.write(row)
	file.close
  
 keeplooping = True
 while keeplooping == True:
  print("1- Add record")
  print("2- View all records")
	print("3- Delete a record")
  print("4- Quit.")
  print()
  selection = input("Enter option: ")
  if selection == "1":
    add_record()
  elif selection == "2":
		view_records()
	elif selection == "3"
		delete_record()
	elif selection == "4"
		keeplooping = False
	else:
		print("Not an option. Press keys [1],[2],[3] or [4], and [Enter]")
		
