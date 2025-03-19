##                         LIST 									##

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


####                                TUPLE                           ###
t1 = (10, 20, True, 'Code', 20, 10)
print(t1, type(t1))

print(t1[0]) #10
print(t1[4]) #20
print(t1[-1]) #10  last element

#t1[2] = 30 - TypeError: 'tuple' object does not support item assignment - immutable
##unpacking the tuple
t2 = (100, 200, 300, 400)
e1, e2, e3, e4 = t2 # if 4 values arent given to unpack ValueError: too many values to unpack (expected 3)
print(f"e1:{e1}, e2:{e2}, e3:{e3}, e4:{e4}")

tup1 = (10, 20)
tup2 = (30, 40)

print(tup1 + tup2) #(10, 20, 30, 40) - concatenates all the values form both the tuple
tup3 = (50, 60)
print(tup1 + tup2 + tup3)
newTupLength = tup1 +tup2 +tup3
print(len(newTupLength)) #6


#Repeating a tuple
tup4 = ('A') * 4 #AAAA
print(tup4)

tup5 = ('A',) * 4 #('A', 'A', 'A', 'A')
print(tup5)

"""
1. Tuple  can store both homogenous and heterogenous data (data with different DataType and Same DataType)
2. Tuple is an Ordered Collection of Data.List maintains order of insertion in the output
3. Tuple allows storing duplicate values.
4. Tuple is not changable (immutable)
"""


##                        SET                        ##
set1 = {10, 20, 30, 'Code', True}
print(set1)

# set1[1] = 40 #TypeError: 'set' object does not support item assignment
set1.add(300)
print(set1)

set1.remove(True)
print(set1)

#set1.remove("true")
#print(set1)

set1 = {3, 3, 4, 4, 2, 1}
set2 = set([4, 5, 6, 3]) #Initializing set usin set() method

combined = set1.union(set2)
print(combined)

intersection = set1.intersection(set2)
print(intersection)
"""
1. Set  can store both homogenous and heterogenous data (data with different DataType and Same DataType)
2. UnOrdered Collection of Data.Set does not maintains order of insertion in the output
3. Set does not allow storing duplicate values.
4. Set is changable (mutable) - can add mor remove - Note that while a Python set itself is mutable (we can remove items from it or add new ones), its items must be immutable data types, like integers, floats, tuples, or strings.
Unindexed- we can't access the items with [i] as with lists
Iterable-we can loop over the items of a set
"""

##                        DICTIONARY   key-value pairs                            ##
dictionary1 = {
	'name' : 'Apoorva',
	'age' : 28,
	'hobbies' : ('Dancing', 'Painting', 'Running', 'Walking', 'Cooking'),
	'number': 123456789,
	'surname' :'Apoorva' 
}

print(dictionary1)
dictionary1['surname'] = 'Natesh'
print(dictionary1['surname'])

hobbies = dictionary1.pop('hobbies')
print(hobbies)
del dictionary1['number']
print(dictionary1)

"""
1. stores both homogenous adn heterogenous data
2. Ordered colletion of Data
3. Allows dulpicate values for values but not duplicate keys
4. Dictionary is mutable
"""

for i in dictionary1.values():
	print(i,end=" - ") # Apoorva-28-Natesh-

for i in dictionary1.keys():
	print(i, end=" : ")

print()

for i in dictionary1.items():
	print(i)