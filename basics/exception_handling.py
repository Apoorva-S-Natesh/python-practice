def add(a,b):
	print("start")
	print(a/b)
	print("End")

try:
	add(5, 3.0)
except ZeroDivisionError:
	print("ZeroDivisionError occured") # add(5, 0)
	print("give a non-zero denominator")
except NameError:
	print("NameError occured and handled") # a/c in the method
	print("ENter a valid value")
except TypeError:
	print("TypeError occured") # add(5, 'c')
	print("Enter a valid type : Number")
except:
	print("Some other Error occured") # Any other exception
else:
	print("There is no exception")
finally:
	print("Cleaning the resources")

print("other tasks")


##############     				Custom exception                  #######
class InvalidAge(Exception):
	pass

def checkAge(age):
	if age < 18:
		raise InvalidAge("Age has to be greater then 18")
	elif age > 100:
		raise InvalidAge("Age has to be between 18 to 100")
	
print("Enter the age")
try:
	age = int(input())
except ValueError:
	print("Age should be a valid number")
else:
	try:
		checkAge(age)
	except InvalidAge as e:
		print("Invalid age Exeption detials:",e) #e has the detail of the exception, "Age has to be greater then 18"
finally:
	print("Submit documents for verification")