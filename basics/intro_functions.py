def add(a,b):
	print('Inside add method')
	print('Addition is:',a+b)
add(10, 30)
print('Enter a number for addtion')
n1 = int(input())
print("5 more to this number is")
add(n1, 5)

def subtract(num1, num2):
	if(num1>num2):
		result=num1-num2
	elif(num2>num1):
		result=num2-num1
	else:
		result = 0
		print ("Numbers are same")
	return result

print("subtraction result is",subtract(20,20))


def multiply(num1, num2):
	sum=0
	for i in range(num2): #start is considered as 0
		sum += num1
	return sum

print("The multiplication is:",multiply(5, 3))

for i in range (11,2,-3):
	print(i)
for i in range(5, 10):
	print(i, end=" ")
print()

def divide(num1, num2):
	quotient = 0
	while (num1 > 0):
		num1 = num1-num2
		quotient += 1
	return quotient 

print("Quotient is:",divide(10,2))

def table(num):
	for i in range(1, 11):
		#print(f"{num} x {i} = {i*num}", end=" ")
		print(i*num, end=" ")


num=int(input("Enter the number to print table :"))
table(num)