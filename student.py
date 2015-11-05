class Student:
	def __init__(self, name, surname, department):
		self.name = name
		self.surname = surname
		self.department = department
		
	def __str__(self):
		return '%s %s %s' % (self.name, self.surname, self.department)
	
	def search(self, what):
		return ('%s' % self).decode('utf-8').lower().find(what.decode('utf-8').lower()) != -1