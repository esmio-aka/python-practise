# Your code goes here

# Step 1: Prompt the user to enter two numbers
# Use the input() function to get user input and store it in two separate variables
uinput = input('Enter two numbers: ').split()

# Step 2: Store the user's input in two separate variables
x, y = float(uinput[0]), float(uinput[1])

# Step 3: Perform addition, subtraction, multiplication, and division operations
# Use the appropriate operators (+, -, *, /) to perform the operations
addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y

# Step 4: Print the results of each operation
# Use the print() function to display the results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
