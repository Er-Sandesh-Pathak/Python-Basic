# Objective: Build a basic calculator that can perform addition, subtraction, multiplication, and division.
# Skills: Functions, user input.
# Steps:
    # Create functions for each operation.
    # Take user input for the operation and numbers.
    # Perform the calculation and display the result.

# Simple Calculator

#defining function for addition, subtraction, multiplication, and division
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y == 0:
        return "We cannot divide by zero"
    return x / y


#frame
print(" \n|----------Welcome to Made in Nepal calculator.------------|")
print(" __________Select operation that you want use________________\n")

#1/2/3/4 for visualization(so that user know 1234 means which which)
print(" 1. Addition")
print(" 2. Substraction")
print(" 3. Multiplication")
print(" 4. Division")

choice = input("\nEnter your choice-->(1/2/3/4) := ")


print(" ------Thank you. Enter your two numbers, please----")
num1 = float(input("\nNumber 1 := "))
num2 = float(input("Number 2 := "))



if choice == "1":
    task = "Addition"
    result = add(num1, num2)
    # print("Addition of", num1, "and" ,num2, "is : ")
    # print(result)

elif choice == "2":
    task = "Substraction"
    result = sub(num1, num2)
    # print("Substraction of", num1, "and" ,num2, "is : ")
    # print(result)

elif choice == "3":
    task = "Multiplication"
    result = mul(num1, num2)
    # print("Multiplication of", num1, "and" ,num2, "is : ")
    # print(result)

elif choice == "4":
    task = "Division"
    result = div(num1, num2)
    # print("Division of", num1, "and" ,num2, "is : ")
    # print(result)
else:
    print("Invalid choice. Choose 1 or 2 or 3 or 4 only")
    
# print("=", result)
print(task, "of", num1, "and", num2, "is := ", result)
print("_________________________________________________")