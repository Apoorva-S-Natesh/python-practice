class Demo:
		def __init__(self):
			self.name = "Apoo"
d1 = Demo()
print(d1.name) #Accessing public property outside the class - Allowed

class Demo1(Demo):
	def disp(self):
		print(self.name) #Accessing public property inside child class - allwed

d2 = Demo1()
d2.disp()

class Code:
	def display(self):
		print(d1.name)

c = Code()
c.display() #Accessing public property inside Non-child class - allowed