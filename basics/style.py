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

#PRINTING
# Printing on same line
"""
By default print() ends with a newline, which moves the text cursor to the next line.
but by using end=" ", Pythons ends a line with a space instead of new line. this way the next print() statement will
appear on the same line. end parameter by default is set to \n
"""
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
print (type(b"hello"))
print(id(name)) #printing the memory address of the object

#formatting a float while printing
average = 34.98604853
print(f"The average is : {average:.2f}")
info= """I'm working at "Microsoft" """
print(info)
poem = '''Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are! '''
print(poem)
data = "Coding"+"Game"
print(data)

#STRING MANIPULATION
text = "I love Programming. It's fun"
print("Length of the text is: ", len(text)) #Length of the text is:  28
print("Character at index -1 is: ", text[-1]) #Character at index -1 is:  n
slicing_text = text[3:]
print("Slicing text from index 2: ", slicing_text) #Slicing text from index 2:  ove Programming. It's fun
print("Slicing the text with giving start and end index: ", text[5: 10]) #Slicing the text with giving start and end index:  e Pro
print("Finding a substring", text.find("o")) #3
print("o" in text) #true
print("replacing the text", text.replace("o", "e")) #I leve Pregramming. It's fun
#text[1] = 'p' #TypeError: 'str' object does not support item assignment
#print(text)
text1 = "ooooo"
print(f"id of {text[3]} and {text[9]} is {id(text[3])} and {id(text[9])}.THEY ARE THE SAME")
print(f"Address of o in text1 is {id(text1[0])} | {id(text1[3])}")
print("The adress of all the o is th o is same! Because everything in Python is an object.") 
s1='	code	'
print(s1)
print(s1.strip()) #removes the leading and trailing spaces
s2 = '---World---'
print(s2)
print(s2.lstrip('-'))
print(s2.rstrip('-'))
print(s2.strip('-')) #removes the leading and trailing spaces