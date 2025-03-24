class Employee :
	company_name ="Code" #class level variable

	def work(self):
		print(self.name,"is working.")
	
	def play(self):
		print(self.name,"is playing.")

e1 = Employee()
e1.name = 'Apoo' #instance Variable - variables which are present inside an object
e1.id = 1013
e1.work()

e2 = Employee()
e2.name = 'Apoorva' #code redundency, so should use constructor
e2.id = 4023
e2.work()
e2.play()

''' 
1.Methods present inside a class are called as Instance methods
2. For instance methods, self parameter is mandatory
3. self is like the this keyword in java - Self always holds the address of current object
4. each object will have its own copy of instance variable
'''