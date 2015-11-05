from student import *
from utils import *

students = [
	Student("Dogan", "Derya", "Computer Engineering"),
	Student("Goksel", "Pirnal", "Computer Engineering"),
] 

print "Pick the number"
print "[1] List of students"
print "[2] Add student"
print "[3] Remove student"
print "[4] Search student"
print "[5] Exit"

while 1:
	press = Utils.readLine('pick')
	
	if press == '1':
		Utils.printList(students)
		
	elif press == '2':
		name = Utils.readLine('name')
		surname = Utils.readLine('surname')
		department = Utils.readLine('department')
		students.append(Student(name, surname, department))
		
	elif press == '3':
		found = Utils.searchInList(Utils.readLine('search for delete'), students)
		sure = Utils.readLine('deleting \n-%s\ny for yes, n for no' % found[0])
		if (sure == 'y' or sure == 'yes'):
			students.remove(found[0])
			
	elif press == '4':
		found = Utils.searchInList(Utils.readLine('search'), students)
		if len(found) != 0:
			Utils.printList(found)
		else:
			print "Can't find the student"
			
	elif press == '5':
		break