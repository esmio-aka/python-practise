# Step 1: Prompt the user to enter a temperature value
temp_value = float(input("Enter the temperature value: "))

# Step 2: Ask the user to specify whether the temperature is in Fahrenheit or Celsius
temp_unit = input("Is the temperature in Fahrenheit (F) or Celsius (C)? ").strip().lower()

# Step 3: Perform the conversion based on the user's input
if temp_unit == "f":
    # Convert from Fahrenheit to Celsius
    celsius = (temp_value - 32) * 5/9
    converted_unit = "Celsius"
elif temp_unit == "c":
    # Convert from Celsius to Fahrenheit
    fahrenheit = (temp_value * 9/5) + 32
    converted_unit = "Fahrenheit"
else:
    print("Invalid input. Please specify 'F' for Fahrenheit or 'C' for Celsius.")
    exit()

# Step 4: Display the converted temperature
print(f"The temperature in {converted_unit} is {celsius if temp_unit == 'f' else fahrenheit}")