try:
	file1 = open("demo.txt", 'r')
	data = file1.read()
	print(data)
except FileNotFoundError:
	print("The file wasnt found")
except NameError:
	print("Name error")
finally:
	file1.close()

# with open("example.txt", "w") as file:
#     file.write("Hello World!")
'''
The with statement automatically closes the file after you’ve completed writing it.

Under the hood, the with statement replaces this kind of try-catch block:

f = open("example.txt", "w")

try:
    f.write("hello world")
finally:
	f.close()

readlines() method reads all the lines of the file and returs them as a list of strings, each string represents a line.
'''

# try:
# 	file2 = open("demo.txt", 'w')
# 	file2.write("Adding data into demo.txt file") # Data will be replaced with this data
# finally:	
# 	file2.close()

# file3 = open("demo.txt", 'a')
# file3.write("Adding new data to the file with append.\n")
# file3.close()

'''
'r' Read (open the file for reading).
'w' Read (open the file for writing).
'a' Read (open the file for appending).

'''