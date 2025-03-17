rows = int(input("Enter rows:"))
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
        

""" this can be written in a conscise way """
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