"""
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

"""

li = [10, 20, 30, 40]

iterator = iter(li) #iter builtin method
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Even strings are iterable objects, and can return an iterator
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

class Counter:
	def __init__(self, limit):
		self.count = 0
		self.limit = limit

	def __iter__(self):
		return self
	
	def __next__(self):
		if self.count < self.limit:
			self.count += 1
			return self.count
		else:
			raise StopIteration

c1 = Counter(5)
print(c1.__iter__())
print(c1.__next__())
print(c1.__next__())
print(c1.__next__())
print(c1.__next__())