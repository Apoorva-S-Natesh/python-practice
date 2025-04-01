from abc import ABC, abstractmethod

'''An Object for empty abstract class  can be created'''
class Bird(ABC):
	pass
b1 = Bird()
print (b1)

"""
If the abstract class contains abstract method, then object for that 
abstract class cannot be created and abstract method cannot be invoked."""

class Animal(ABC):
	@abstractmethod
	def eat(Self):
		pass

#a1 = Animal()

''' If abstract class contains only concrete methods, then object can be created
 and concrete method can be invoked'''
class Pets(ABC):
	def eat(self):
		print("Pet is eating")

p1 = Pets()
p1.eat()


'''
If a class is derived from abstract class and not given body for all abstract methods
in the child class then the child class object cannot be created
'''
class Vehicle(ABC):
	@abstractmethod
	def gears(self):
		pass
	@abstractmethod
	def breaks(self):
		pass

class Car(Vehicle):
	def wheels(self):
		print("Car has 4 wheels")

#c1 = Car() #Output TypeError

class Cycle(Vehicle):
	def gears(self):
		print("Cycle No gears")

	def breaks(self):
		print("Cycle Has 2 breaks")

c2 = Cycle()
"""
ABC - Abstract Base Class 
"""
	


