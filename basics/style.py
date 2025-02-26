print('Hello World')

# Performing addition in Scripting style (small script)
a = 10
b = 20
print("Addition of a and b is:", a+b)

'''
1. Python is dynamically typed programming language in which programmer doesnt 
have to mention datatype while declaring variables.
2. The datatype for variables will be assigned by python based on value stored into the variables.

3. Pyhton is one of the most concise programming language.
'''
# Performing addition in Procedular Style
def add (c, d):
	print("Addition of 2 numbers:", c+d)

'''
Creating a method, using def keyword. Observe the style. Wrapping the logic inside a procedure.  

'''	
add(1, 50) #callign the method

# Performing addition in Object Oriented Style
class Demo:
	def add(self, a ,b):
		print('Addtion is:', a+b)
	
d1 = Demo()
d1.add(10,100)

'''
Creatig a class using class keyword with a method add inside.
Creating the object d1 of Demo class.
calling the method using the object.

Python gives importance to intentation.
'''

# Printing on same line
print("Hello", end=" ") 
print("Jello!")
print("Hello", end="-") 
print("Mello!")
print("Hello", end="\t") 
print("Fello!")
print("Hello, Python!\t Welcome to the worlds of \n JELLO.")
name = "Jello"
print(f"Hello, {name}!") # String formatting with f and {}
print(type(name))
"""
By default print() ends with a newline, which moves the text cursor to the next line.
but by using end=" ", Pythons ends a line with a space instead of new line. this way the next print() statement will
appear on the same line. end parameter by default is set to \n
"""