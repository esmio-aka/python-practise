# Your code goes here

# Step 1: Prompt the user to enter a temperature value
# Use the input() function to get the temperature as a number and store it in a variable
temperature = float(input("Enter the temperature to be converted: "))

# Step 2: Ask the user to specify whether the temperature is in Fahrenheit or Celsius
# Use the input() function to get the user's choice and store it in a variable
scale = input("Is temperature in Fahrenheit (F) or Celsius (C)?: ")

# Step 3: Perform the conversion based on the user's input
# Use appropriate formulas to convert between Fahrenheit and Celsius
# You may need to use type casting to ensure consistent data types
if "F" in scale:
    temperature = (temperature - 32) * 5/9
    unit = "Celsius"
else: 
    temperature = (temperature * 9/5) + 32
    unit = "Fahrenheit"

# Step 4: Display the converted temperature
# Use the print() function to show the result
print(f"The temperature in {unit} is {temperature}")