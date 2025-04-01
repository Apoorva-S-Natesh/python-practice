class Person:
	def __init__(self, name, age):
		self.name = name
		self.__age = age #private variable (__name), (_name) - protected variable

	def get_age(self):
		return self.__age
	
	def set_age(self, newage):
		self.__age = newage

p1 = Person("Apoorva", 28)
print(p1.name)
#print(p1.__age)-Error
print(p1.get_age()) # 28
p1.set_age(29)
print(p1.get_age()) # 29