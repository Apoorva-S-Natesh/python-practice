##           Inheritance - Syntax : class ChildClass_Name(Parent_Class)     ##

# Single Inheritence #

class Demo1:
	def display1(self):
		print("inside parent display")

class Demo2(Demo1):
	def display2(self):
		print("inside child1 display")

d2 = Demo2()
d2.display1()
d2.display2()

##		Heirarchial Inheritance   ##  One parent class, many child class
class Demo3(Demo1):
	def display3(self):
		print("Inside child2 display")

d3 = Demo3()
d3.display1()
d3.display3()

""" If you add a method in the child class with the same name as a function in 
the parent class, the inheritance of the parent method will be overridden. """

###		Multilevel Inheritance ###  Grandparent <-- parent <-- child

class Demo4(Demo3):
	def display4(self):
		print("Inside demo4 display - child of child")

d4 = Demo4()
d4.display1()
d4.display3()
d4.display4()

####	Multiple Inheritance ####	One deriver class - more than one derived class
#### using MRO Technique

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
	pass

student1 = Student("Apoo", "Natesh")
student1.printname()


