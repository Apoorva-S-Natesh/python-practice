class GreatGrandParent:
	def cook(self):
		print("Grandparent cooks for hours")

class GrandParent(GreatGrandParent):
	def cook(self):
		print("Grandparent cooks Biryani")

class Parent(GrandParent):
	def cook(self):
		print("Parent cooks Paneer")

class Child(Parent):
	def cook(self):
		print("Child cooks Maggie")
		super().cook() # calls cook method od parent
		super(Parent,self).cook() #Method chaining - call cook of parent of parent
		""" Output: 
			Child cooks Maggie
			Parent cooks Paneer      
			Grandparent cooks Biryani"""
		super(GrandParent,self).cook()
		"""
		Child cooks Maggie
		Parent cooks Paneer        
		Grandparent cooks Biryani  
		Grandparent cooks for hours
		"""

c = Child()
c.cook()