##                     CLASS COPONENTS	- class attributes, Instance attributes, static methods, class methods                     ##
class Student:
	college_name = "ABC University"  # class attribute or variable

	def __init__(self, name, age, id):
		self.name = name  # Instance Attribute or variable specific to each instance of the class
		self.age = age
		self.id = id

	def attend_class(self):
		print(f"{self.name} from {Student.college_name} is attending class.")  # accessing class attribute using class name and instance attribute using object reference

	@staticmethod
	def university_facility(library, labs):
		print(f"{library} and {labs} present at level 0 and 1")

	""" 
	A static method does not receive an implicit first argument. A static method 
	is also a method that is bound to the class and not the object of the class. 
	This method can’t access or modify the class state. It is present in a class 
	because it makes sense for the method to be present in class. 
	Use static method when the method doesnt require any info about instance or class-level data
	"""

	@classmethod
	def change_uni_name(cls, new_name):
		cls.college_name = new_name # Modifying class attribute using class method

student1 = Student('Apoo', 28, 'A243')
student2 = Student('John', 40, 'F345')

student1.attend_class()
student1.attend_class()

print(student1.college_name) #accesing class arrtibute using reference variable
Student.university_facility("Arts", "Biotech") # accessing static method using  class name
student1.university_facility("Law", "Architecture") # accessing static method using object reference
Student.change_uni_name("XYZ University") #changing the class attribute using a class method
print(student2.college_name)
student1.change_uni_name("MNO University") # Accessing class method using an object reference
print(student2.name,"studies at",student2.college_name)
print(student1.name,"studies at",student1.college_name)

"""
Class method vs Static Method
The difference between the Class method and the static method is:

* A class method takes cls as the first parameter while a static method needs no specific parameters.
* A class method can access or modify the class state while a static method can’t access or modify it.
* In general, static methods know nothing about the class state. They are utility-type methods that 
take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
"""