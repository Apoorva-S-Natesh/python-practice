def decor(function):
	def inner(name):
		if name == 'Apoo':
			print(name,"likes donut")
		else:
			return function(name)
	return inner

@decor
def process(name):
	print(name, 'likes fries')

process('Hello') 
"""
when process is called, the control goes to decor function
"""
process('Jello')
process('Apoo')
process('Jello')

def smartdiv(function):
	def inner(a,b):
		if (b == 0):
			print("Cannot divide by 0")
		else:
			return function(a,b)
	return inner

@smartdiv
def div(a, b):
	print(a, b)

div(10, 2)
div(20,5)
div(10, 0)
div(30, 5)


def shout(word="yes"):
    return word.capitalize()+"!"

print(shout())
# outputs : 'Yes!'

# As an object, you can assign the function to a variable like any other object 
scream = shout

# Notice we don't use parentheses: we are not calling the function,
# we are putting the function "shout" into the variable "scream".
# It means you can then call "shout" from "scream":

print(scream())
# outputs : 'Yes!'

# More than that, it means you can remove the old name 'shout',
# and the function will still be accessible from 'scream'

del shout
try:
    print(shout())
except NameError as e:
    print(e)
    #outputs: "name 'shout' is not defined"

print(scream())
# outputs: 'Yes!'
"""
You’ve seen that functions are objects. Therefore, functions:
can be assigned to a variable
can be defined in another function
That means that a function can return another function.

"""
def getTalk(kind="shout"):

    # We define functions on the fly
    def shout(word="yes"):
        return word.capitalize()+"!"

    def whisper(word="yes") :
        return word.lower()+"..."

    # Then we return one of them
    if kind == "shout":
        # We don't use "()", we are not calling the function,
        # we are returning the function object
        return shout  
    else:
        return whisper

# How do you use this strange beast?

# Get the function and assign it to a variable
talk = getTalk()      

# You can see that "talk" is here a function object:
print(talk)
#outputs : <function shout at 0xb7ea817c>

# The object is the one returned by the function:
print(talk())
#outputs : Yes!

# And you can even use it directly if you feel wild:
print(getTalk("whisper")())
#outputs : yes...

"""
If you can return a function, you can pass one as a parameter

"""
def doSomethingBefore(func): 
    print("I do something before then I call the function you gave me")
    print(func())

doSomethingBefore(scream)
#outputs: 
#I do something before then I call the function you gave me
#Yes!

# A decorator is a function that expects ANOTHER function as parameter
def my_shiny_new_decorator(a_function_to_decorate):

    # Inside, the decorator defines a function on the fly: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    def the_wrapper_around_the_original_function():

        # Put here the code you want to be executed BEFORE the original function is called
        print("Before the function runs")

        # Call the function here (using parentheses)
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original function is called
        print("After the function runs")

    # At this point, "a_function_to_decorate" HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before and after. It’s ready to use!
    return the_wrapper_around_the_original_function

# Now imagine you create a function you don't want to ever touch again.
def a_stand_alone_function():
    print("I am a stand alone function, don't you dare modify me")

a_stand_alone_function() 
#outputs: I am a stand alone function, don't you dare modify me

# Well, you can decorate it to extend its behavior.
# Just pass it to the decorator, it will wrap it dynamically in 
# any code you want and return you a new function ready to be used:

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()
#outputs:
#Before the function runs
#I am a stand alone function, don't you dare modify me
#After the function runs


############# Decorator with parameter
def repeat_decorator(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator

@repeat_decorator(3)
def say_hello():
      print("Hello, Jello")     

say_hello()