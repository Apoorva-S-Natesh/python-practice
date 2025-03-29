## 				1. Method Overloading(stimulated) alone is supported in Python, just like Javascript   ##

def display():
	print("No arguments")

def display(a):
	print("One argument",a)

def display(a,b):
	print("two arguments",a,b)

def display(a,b,c):
	print("Three arguments", a,b,c)

#display() #TypeError: display() missing 3 required positional arguments: 'a', 'b', and 'c'
#display(30, 50) #Error: Missing 1 required positional argument
display(10, 30 , 50)

# Polymorphism achieved through args
def add(datatype, *args):

    if datatype == 'int':
        answer = 0

    if datatype == 'str':
        answer = ''

    for x in args:
        answer = answer + x

    print(answer)

add('int', 5, 6)
add('str', 'Hi ', 'Apoorva')


###  	              2.Method OverRiding                ###

class Parent:
	def cook(self):
		print("Cooking Pasta")
	def learn(self):
		print("Learning Python")

class Child(Parent):
	def play(self):
		print("Playing chess")
	def learn(self):
		print("Learning Java")

child1 = Child()
child1.cook()
child1.learn()
print(child1) # <__main__.Child object at 0x000001C6CAB06900> - String representation of the address of the object, __str__() will be automatically called

"""
1.The method which is derived from Parent class and used as it is in the child class - Inherited Method 
	- cook() in above example
2. The method which is only available for child class and not for the parent class - Speialized method
	- learn() in the above exmample
3. The method which is derived form parent class and is modified inside the child class to give its own method body
	- learn() in the above exmaple
"""

##                 		3.Operator Overloading		 				##

'''
Magic methods / dunder Methods - methods which have suffix and prefix as '__' double underscore
These methods are not called by the programmer but will be called automatically. eg __init__()
__str__() -trying to print object reference

'''

class Student:
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return self.name
	def __add__(self, other): #ovreriding the + operator when '+' is used on obejct references, __add__() is called
		return self.name + other.name
	def __sub__(self, other):
		return self.name+other.name
	#def __div__(self,other): # TypeError: unsupported operand type(s) for /: 'Student' and 'str'
	#	return self.name+other.name
	def __truediv__(self,other):
		return self.name + other.name
s1 = Student("Apoo")
s2 = Student("rva")
print(s1) #Hello insted of string of the address, when printing the object reference then __str__() is called
#print(s1 + s2) #TypeError: unsupported operand type(s) for +: 'Student' and 'Student' when __add__() is not overridden
print(s1 + s2) #Apoorva
print("hello"+"World") 
print(s1-s2)
print(s1/s2)
"""One Operator performing multiple tasks. '+' can perform addtion, perfom string concatenation"""


##						4.Duck Typing							##

class Parrot:
	def fly(self):
		print("Parrot is flying high in the sky!")
	
class Airplane:
	def fly(self):
		print("Airplane is taking off!")

#Function using duck typing
def make_it_fly(thing):
	thing.fly()

parrot = Parrot()
airplane = Airplane()

make_it_fly(parrot)
make_it_fly(airplane)

"""
Duck typing is based on the saying, "If it looks like a duck and quacks like a duck, it must be a duck"
here it means that any object that has the needed behavior can be used withot worrying about its exact type

"""

## eXample 2
class Add:
	def calculate(self, a, b):
		print(a + b)

class Mul:
	def calculate(self,a, b):
		print(a * b)

class Div:
	def calculate(self, a,b):
		print(a / b)

def operate(operator):
	operator.calculate(40, 10)

operate(Add())
operate(Mul())
operate(Div())