# Your code goes here

# Step 1: Prompt the user to enter an amount in one currency
# Use the input() function to get the amount as a number and store it in a variable
amount = float(input("Enter currency amount: "))

# Step 2: Ask the user to select the source and target currencies
# Use the input() function to get the user's choice and store it in a variable
sta_curr = input("Enter the source and target currensies (e.g., USD to EUR): ")
source_currency, to, target_currency = sta_curr.strip().split()

# Step 3: Retrieve the current exchange rate from a predefined dictionary
# Use a dictionary to store exchange rates (e.g., {'USD to EUR': 0.85, ...})
# Extract the relevant exchange rate based on the user's choice
exch_rate = {
    'USD to EUR': 0.9427,
    'EUR to USD': 1.0604,
    'UAH to EUR': 0.0256,
    'EUR to UAH': 38.4188,
    'UAH to USD': 0.0271,
    'USD to UAH': 36.2664}

re_rate = exch_rate[sta_curr]


# Step 4: Perform the currency conversion and display the converted amount
# Use the exchange rate to convert the amount and print the result
conv_amount = amount * re_rate
print(f"{amount} {source_currency} is {conv_amount} {target_currency}")