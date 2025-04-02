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