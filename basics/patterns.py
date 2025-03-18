rows = int(input("Enter rows:"))
"""
for i in range(1, rows+1):
	print("* " * i)

print()

## Diamond pattern
n = 4  # Number of rows in the upper half

# Upper part of the diamond
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    print("*", end="")
    if i > 0:
        for j in range(2 * i - 1):
            print(" ", end="")
        print("*")
    else:
        print("")

# Lower part of the diamond
for i in range(n - 1, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")
    print("*", end="")
    if i > 0:
        for j in range(2 * i - 1):
            print(" ", end="")
        print("*")
    else:
        print("")
        

n = 4  # Number of rows in the upper half

for i in range(n * 2 - 1):
    spaces = abs(n - 1 - i)
    stars = n - spaces - 1
    print(" " * spaces + "*" + (" " * (2 * stars - 1) + "*" if stars > 0 else ""))

n = 4  # Number of rows in the upper half

# Upper half
for i in range(n):
    print(" " * (n - i - 1) + "*" + (" " * (2 * i - 1) + "*" if i > 0 else ""))

# Lower half
for i in range(n -1, -1, -1):
    print(" " * (n - i - 1) + "*" + (" " * (2 * i - 1) + "*" if i > 0 else ""))
"""

## Hill pattern hollow inside
for i in range(rows):
    for j in range(i, rows-1):
        print("-", end=" ")
    for k in range(i+1):
         print("*" if(k==0 or i==rows-1) else " ", end=" ")
    for m in range(i):
          print("*" if m==i-1 or i==rows-1 else " ",end=" ")
    print()
    
## inverted Hill
for i in range(1, rows):
     for j in range(i):
          print("-", end=" ")
     for k in range(i+1, rows):
          print("*", end=" ")
     for m in range(i, rows):
          print("*", end=" ")
     print()
    
print()

### Right Pascal Trinagle ###
for i in range(rows):
     for j in range(i+1, rows):
          print("-", end=" ")
     for k in range(i+1):
          print("*", end=" ")
     print()
for i in range(1, rows):
     for j in range(i):
          print("-", end=" ")
     for k in range(i,rows):
          print("*", end=" ")
     print()