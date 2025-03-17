li1 = [10, 20, 10, 'Code', True, 33.6]
print(li1, type(li1))

print(li1[0])
print(li1[1])

li1[5] = 66.7 #Lsit is mutable
print("after update",li1)

"""
1. List  can store both homogenous and heterogenous data (data with different DataType and Same DataType)
2. List is an Ordered Collection of Data.List maintains order of insertion in the output
3. List allows storing duplicate values.
4. Lists are changable (mutable), Strings are immutable
"""

#                      LIST METHODS	                       #

#Adding element into list
list1 = []
list1.append(100) #adds the element to the end of the list
list1.append(50)
print(list1)

print(list1.insert(1, 400)) #output : none - insert() doesnt return anything so prints none #list1 is now [100, 400, 50]
list1.insert(1, 500) # [100, 500, 400, 50]
print(list1)

element1 = list1.pop()
print(element1) #50
print(list1) # [100, 500, 400]

print(list1.pop(1)) # 500
print(list1) # [100, 400]

#del keyword
del list1[0] # del deletes an item at a specific position or the entire list
print(list1) # [400]

del list1 # deletes whole object from memory
#print(list1) # Output : NameError: name 'list1' is not defined.