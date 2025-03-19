"""num1 = input()
num2 = input()
print(f"Addition of {num1} and {num2} is: {num1+num2}") #Concatenation happens here since the input method always accepts as a String"""
'''Accept the input from use and typecase to int and store it into num as input always accepts String'''

"""num3 = int(input("Enter number:")) #num3 = int(input()) but if we need to give a prompt then can be given as an argument for input()
num4 = int(input())
print(f"Addition of {num3} and {num4} is: {num3+num4}")"""

'''because of int conversion the  input will be trimmed internally'''

s1 = input("enter a string with leading and trailing spaces: ").strip()
print(s1)

num1 = int(input("Enter num1  :"))
num2 = int(input("Enter num2  :"))
choice = input("Add-1, Sub-2, Mul-3, Div-4, SquareOfnumber-5, FloorDiv-6, Modulus-7 ")
if choice == '1':
    print("Addition is:", num1 + num2)
elif choice == '2':
    print("Subtraction is:", num1 - num2)
elif choice == '3':
    print("Multiplication is:", num1 * num2)
elif choice == '4':
    print("Division is: ",num1 / num2)
elif choice == '5':
    print("Square of num1 is: ",num1 ** 2)
    print("Square of num2 is: ",num2 ** 2)
elif choice == '6':
    print('Floor Division is: ',num1 // num2)
elif choice == '7':
    print('Remainder is: ',num1 % num2)
else:
    print("Invalid Choice...!!")
    

##### LOgical Operators ######
print(True and False)
print(True and True)
print(10 > 5 and 70 == 70)
print(False and True)
print(40!=0 and 60==60)
print(not True)

userData = input("Enter list of elements separated by space: ")
li = userData.split() #String to list userData.split('-')
print(li)
newli = []
for i in li:
	newli.append(int(i)) 
    
print(sum(newli)/len(newli)) #average