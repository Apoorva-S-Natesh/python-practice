##           Inheritance - Syntax : class ChildClass_Name(Parent_Class)     ##

# Single Inheritence #

class Demo1:
	def display1(self):
		print("inside parent display")

class Demo2(Demo1):
	def display2(self):
		print("inside child1 display")

print("Single inheritance")
d2 = Demo2()
d2.display1()
d2.display2()

##		Heirarchial Inheritance   ##  One parent class, many child class
class Demo3(Demo1):
	def display3(self):
		print("Inside child2 display")

print("Heirarchial inheritance")
d3 = Demo3()
d3.display1()
d3.display3()
print()

""" If you add a method in the child class with the same name as a function in 
the parent class, the inheritance of the parent method will be overridden. """

###		Multilevel Inheritance ###  Grandparent <-- parent <-- child

class Demo4(Demo3):
	def display4(self):
		print("Inside demo4 display - child of child")

print("Multilevel inheritance")
d4 = Demo4()
d4.display1()
d4.display3()
d4.display4()
print()

####	Multiple Inheritance ####	One derived class - more than one derived class
#### using MRO Technique - Method Resolutions Order - python defines the order in which methods are searched in a multiple inheritance scenario.// 

class Demo5():
	def display5(self):
		print("Inside demo5 display")
	def display1(self):
		print("Inside Demo6 display1")

class Demo6(Demo1, Demo5):
	def display6(self):
		print("Inside demo5 display")

print("Multiple inheritance")
d6 = Demo6()
d6.display1()
d6.display5()
print(Demo6.__mro__) # To check the mro, how clsses check for a method
#Output : (<class '__main__.Demo6'>, <class '__main__.Demo1'>, <class '__main__.Demo5'>, <class 'object'>) , interchange Demo1 and Demo5 in derived class and the mro changes
print()

"""
when trying to create multiple inheritance with a class Demo2 that was already inheriting from Demo1
TypeError
  File "E:\Python\basics\inheritance.py", line 43, in <module>
    class Demo5(Demo1, Demo2):
        def display5():
                print("Inside demo5 display")
TypeError: Cannot create a consistent method resolution order (MRO) for bases Demo1, Demo2 
"""

class A:
    def rk(self):
        print("In class A")

class B(A):
    def rk(self):
        print("In class B")

r = B()
r.rk()
print()
"""In the above example the methods that are invoked is from class B but not from class A, and this is due to Method Resolution Order(MRO). 
The order that follows in the above code is- class B – > class A ."""



### Calling of emthods and constructors using MRO ##
class Test1:
	def __init__(self):
		self.x =100

class Test2:
	def __init__(self):
		self.x=200

class Test3(Test2, Test1):
	pass

t3 = Test3()
print(t3.x) #200 would be 100 if class Test3(Test1, Test2)
print(Test3.__mro__) #Output : (<class '__main__.Test3'>, <class '__main__.Test2'>, <class '__main__.Test1'>, <class 'object'>)
print()

class Test5:
	def __init__(self, x):
		self.x = x

class Test4(Test5):
	def __init__(self,x, y):
		super().__init__(x)
		self.y=y

	def add(self):
		print("addition is: ",self.x + self.y)

t4 = Test4(3,5)
t4.add()
### MRO and super()
"""
class Example1:
	def __init__(self):
		self.x = 100

class Example2():
	def __init__(self):
		self.x = 200
		super().__init__()

class Example3(Example2, Example1):
	pass

ex3 = Example3()
print("x is",ex3.x) # 100
# MRO and super()
# Example3 --> Example2 --> Example1 --> Object 
"""
""" In the above example: MRO sequence is Example3 ---> Example2 ---> Example1 
since Example2 doesnt have a base class, Example1 constructor will be called"""

class Example1:
	def __init__(self):
		self.x = 100
		super().__init__() # This super will call next class constructor as per MRO

class Example2():
	def __init__(self):
		self.x = 200
		super().__init__() # This super will call next class constructor as per MRO

class Example3(Example1, Example2):
	pass

ex3 = Example3()
print("x is",ex3.x) # 200 
# MRO and super()
# Example3 --> Example1 --> Example2 --> Object