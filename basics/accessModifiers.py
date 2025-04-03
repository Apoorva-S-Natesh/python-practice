class Demo:
		def __init__(self):
			self.name = "Apoo"
			self._lastname = "Natesh" # Protected variable
			self.__middleName = "Somanahally" #pricvate vriable

		def display(self):
			print(self.name)
			print(self._lastname)
			print(self.__middleName)

		def _protected_method(self):
			print(self.name)
			print(self._lastname)
			print(self.__middleName)

		#def __protected_method(Self):
		#	print(self.name)

d1 = Demo()
d1.display()
print(d1.name) #Accessing public property outside the class - Allowed
print(d1._lastname) # Accessing protected variable outside the class - Allowed
#print(d1.__middleName) # Accessing private variable outside the class - Not allowed
d1._protected_method()

class Demo1(Demo):
	def disp(self):
		print(self.name) #Accessing public property inside child class - allowed
		print(self._lastname) #Accessing protected variable inside child class - allowed
		#print(self.__middleName) # Accessing private variable inside child class - Not allowed

d2 = Demo1()
d2.disp()

class Code:
	def display(self):
		print(d1.name)  #Accessing public property inside Non-child class - allowed
		print(d1._lastname)  #Accessing protected property inside Non-child class - allowed
		print(d1.__middleName) # Accessing private property inside non-shild class - Not allowed
		print (d1._Demo__middleName) # -Name Mangling : Is the process of giving new name to prive variable in the format of : _Classname__VariableName. Private variable accesed outside the class
c = Code()
c.display()


'''
public : When we want to access variable anywhere in the code
protected : When we want to access variable inside the same class and inside child class
private : when we want to access variables only inside the same class

In Python, access modifiers are conventions, not strict enforcement.
Developers can access protected and private members if necessary.
Its only a way to tell a developer how the data has to be used.
'''