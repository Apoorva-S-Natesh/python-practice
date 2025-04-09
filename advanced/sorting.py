arr = [7,3,9,12,11]
n = len(arr)


# Bubble sort  - stops when so swapping happened for an entire loop cycle
"""
for i in range(n-1):
	swapped = False
	for j in range(n-i-1):
		if (arr[j] > arr[j+1]):
			arr[j], arr[j+1] = arr[j+1], arr[j]
			swapped = True
	if not swapped:
		break
"""

#Selction sort

for i in range(n-1):
	min_index = i
	for j in range(i+1, n):
		if arr[j] < arr[min_index]:
			min_index = j
	arr[i], arr[min_index] = arr[min_index], arr[i]


print("Sorted array: ", arr)