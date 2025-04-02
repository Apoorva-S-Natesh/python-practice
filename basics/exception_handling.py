def add(a,b):
	print("start")
	print(a/b)
	print("End")

try:
	add(5, 0)
except:
	print("Exception occured and handled...")
else:
	print("There is no exception")
finally:
	print("Cleaning the resources")

print("other tasks")