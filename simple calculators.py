# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

# Function to perform modulus operation
def modulus(x, y):
    return x % y

# Function to perform exponentiation
def exponentiate(x, y):
    return x ** y

# Main program
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentiate")
    print("7. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", modulus(num1, num2))

        elif choice == '6':
            print(num1, "^", num2, "=", exponentiate(num1, num2))

    elif choice == '7':
        print("Exiting calculator...")
        break

    else:
        print("Invalid input")
