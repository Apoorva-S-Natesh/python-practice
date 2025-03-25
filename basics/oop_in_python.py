class Employee :
	company_name ="Code" #class level variable

	def work(self):
		print(self.name,"is working.")
	
	def play(self):
		print(self.name,"is playing.")

e1 = Employee()
e1.name = 'Apoo' #instance Variable - variables which are present inside an object
e1.id = 1013
e1.work()

e2 = Employee()
e2.name = 'Apoorva' #code redundency, so should use constructor
e2.id = 4023
e2.work()
e2.play()

''' 
1.Methods present inside a class are called as Instance methods
2. For instance methods, self parameter is mandatory
3. self is like the this keyword in java - Self always holds the address of current object
4. each object will have its own copy of instance variable
'''

#########                 Constructors                         ##########
class Office:
	def __init__(self, name, location): #Parameterized constructor
		self.name=name
		self.location=location
	
	def displayInfo(self):
		print(self.name, self.location)

office1 = Office("Code", "Berlin")
office2 = Office("FinanceS hop", "London")
office1.displayInfo()
print(office2.name, office2.location)

class Books:
	def __init__(self): #Default Constructor
		self.name="Python book"
		self.Id=4534

book1 = Books()
book2 = Books()
print(book1.name, book1.Id)
print(book2.name, book2.Id)

"""
__new__ Method
This method is responsible for creating a new instance of a class. It allocates memory and returns the new object. It is called before __init__.


class ClassName:
    def __new__(cls, parameters):
        instance = super(ClassName, cls).__new__(cls)
        return instance
To learn more, please refer to “__new__ ” method

__init__ Method
This method initializes the newly created instance and is commonly used as a constructor in Python. It is called immediately after the object is created by __new__ method and is responsible for initializing attributes of the instance.

Syntax:


class ClassName:
    def __init__(self, parameters):
        self.attribute = value
Note: It is called after __new__ and does not return anything (it returns None by default)
"""