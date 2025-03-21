li = [11, 33,54,32,1,2]
print(li)
li.sort() #in-place sorting - original list is sorted and doesnt return anything or returns null
print(li)

li1 = [11, 4, 1, 2, 64, 23, 65]
print(li1)
li1Sorted = sorted(li1) # doesnt sort the original list, returns the sorted list
print(li1)
print(li1Sorted)

set1 = set(li)
set2 = set(li1)

print(set1.issubset(set2)) #False

s1 = "This is a test. This test is to remove the dot character."
s1 = s1.replace(".", " ")
print(s1)
print(s1.count('This'))
print(s1.count("is")) #4 - since is a part of this also, so cannot use count to count the occurrance of the words
dictionary = {}
s1 = s1.split()
for word in s1:
	if word in dictionary:
		dictionary[word] += + 1
	else:
		dictionary[word] = 1

print(dictionary)

for word in dictionary:
	print(f"{word} : {dictionary[word]}")