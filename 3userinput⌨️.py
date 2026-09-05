# input () = A function that prompts the user to enter data returns the entered data as a string

name = str(input("Enter you name?: "))
age = int(input("how old are you?: "))

print(f"Hello, {name}. You are {age} years old.")

# Exercice

length = float(input("Enter the len: "))
width = float(input("Enter the width: "))

area = length * width
print(f"Area of REctangle is {area}. ")