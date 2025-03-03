num1 = input()
num2 = input()
print(f"Addition of {num1} and {num2} is: {num1+num2}") #Concatenation happens here since the input method always accepts as a String
'''Accept the input from use and typecase to int and store it into num as input always accepts String'''

num3 = int(input("Enter number:")) #num3 = int(input()) but if we need to give a prompt then can be given as an argument for input()
num4 = int(input())
print(f"Addition of {num3} and {num4} is: {num3+num4}")

'''because of int conversion the  input will be trimmed internally'''

s1 = input("enter a string with leading and trailing spaces: ").strip()
print(s1)