# We cannot have more than one return statement in a function
# multiple values from a function can be returned using yield keyword
'''A generator is a special type of function which does not return a single value, 
instead, it returns an iterator object with a sequence of values.'''


# Generator function, used when dealing with large amounts of data sets, that returns an iterator that produces a sequence of values when iterated over.
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


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))

# Output: 4895

'''
When the generator function is called, it does not execute the function body immediately. 
Instead, it returns a generator object that can be iterated over to produce the values.
'''

def display2():
	print("start")
	yield 10
	print("Task2 ")
	yield 20
	print("Task 2")
	yield 30
     
res = display2()
# print(res.__next__()) //res itself is an iterator object, can be directly looped over. No need of __next__() method
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())

for i in res:
    print(i)