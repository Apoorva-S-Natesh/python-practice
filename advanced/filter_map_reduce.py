from functools import reduce

li = eval(input("Enter comma seperated elements: ")) #eval converts comma separated string to tuple directly
print(li) # (10, 20, 30, 40, 50, 60)
print(type(li)) # <class 'tuple'>
print(type(li[0])) # <class 'int'>

li = list(li)
def even(ele):
	if ele % 2 == 0:
		return ele
	
def prime(ele):
	for i in range(2, int(ele*0.5 +1)):
		if ele % i == 0:
			return False
	return True

def cube(ele):
	return ele**3

even_li = list(filter(even, li)) # Filter always returns a filter object so need to conver it to list
print("Even List: ",even_li)
prime_li = list(filter(prime, li))
print("Prime list: ",prime_li)
cube_list = list(map(cube, li))
print("Cube of List: ", cube_list)


def sum(num1, num2):
	return num1+num2

sum_result = reduce(sum, li)
print("Sum of all numbers: ", sum_result)

## Same as
"""
print("Enter comma separated elements: ")
li1 = tuple(map(int, input().split(",")))
print(li1)
print(type(li1))
print(type(li1[0]))

li1 = list(li1)
even_li1 = []

for i in li1:
	if i % 2 == 0:
		even_li1.append(i)

print('Even List: ',even_li1)
"""
