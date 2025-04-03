# We cannot have more than one return statement in a function
# multiple values from a function can be returned using yield keyword

def display():
	yield 10
	yield 30
	yield 40

res = display()
print(res) # <generator object display at 0x000001F7341E5F30>
print(res.__next__()) # 10
print(res.__next__()) # 30
print(res.__next__()) # 40
#print(res.__next__()) # StopIteration
