from sys import stdout
from sys import stdin

class Utils:
	@staticmethod
	def readLine(subject):
		stdout.write('%s: ' % subject) 
		return stdin.readline().strip()
		
	@staticmethod
	def printList(list):
		print '\n'.join(" -" + str(x) for x in list)
		print "count: %s" % len(list)
	
	@staticmethod
	def searchInList(search, list):
		found = []
		for element in list:
			if element.search(search):
				found.append(element)
		return found