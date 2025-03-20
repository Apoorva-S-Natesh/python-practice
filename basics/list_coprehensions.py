"""
List comprehension offers a shorter syntax when you want to create a new list based 
on the values of an existing list.

Syntax:
newlist = [expression for item in iterable if condition == True]
newlist = [expression for control_variable in iterable_object]
"""

list1 = [1, 2, 3, 4, 5, 6]
list2 =[num ** 3 for num in list1]
print([i for i in list1 if i%2 == 0])

print(list2)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# which can be achieved using list-comprehension like
newlist1 =[x for x in fruits if "a" in x]
print(newlist1)

#The iterable can be any iterable object, like a list, tuple, set etc.
newlist3 = [i for i in range(10)]
print(newlist3)

#The expression is the current item in the iteration, but it is also the outcome, which you can 
# manipulate before it ends up like a list item in the new list

newlist4 = [x.upper() for x in fruits]
print(newlist4)

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
newlist5 = [x if x != "banana" else "orange" for x in fruits]
print(newlist5)

#nested list comprehensions
nested_list = [[1, 2,3], [4,5,6], [7,8,9]]
float_list = [num for sublist in nested_list for num in sublist]
print(float_list)

#                 map                       #

def square(ele):
  return ele ** 2

result = map(square, list1) # for each element of list1 gives the square of it
print(result)  # <map object at 0x0000020C6009FCD0>

print(list(result)) # [1, 4, 9, 16, 25, 36]

list4 = ['10', '20', '30', '40', '50', '60', '70']
new_list4 = list(map(int, list4)) # or list(map(float, list4)) or list(map(bool, list4))
print(new_list4)

#        list slicing          #
"""		 Syntax : listname[startIndex : endIndex : steps]    """

print(list4[::]) #list slicing start is 0, end is length-1, duplicating the list
print(list4[::2]) #['10', '30', '50', '70'] :2 steps (steps are based on index)
print(list4[1::]) # ['20', '30', '40', '50', '60', '70'] : start from index 1, steps 0, end default
print(list4[:4:]) # ['10', '20', '30', '40'] : start index 0, end index: 4, steps: 0
print(list4[1:3]) # ['20', '30']
print(list4[1:5:2]) # ['20', '40']