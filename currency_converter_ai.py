# Step 1: Prompt the user to enter an amount in one currency
amount = float(input("Enter currency amount: "))

# Step 2: Ask the user to select the source and target currencies
currency_pair = input("Enter the source and target currencies (e.g., USD to EUR): ")
source_currency, to, target_currency = currency_pair.strip().split()

# Step 3: Retrieve the current exchange rate from a predefined dictionary
exchange_rates = {
    'USD to EUR': 0.9427,
    'EUR to USD': 1.0604,
    'UAH to EUR': 0.0256,
    'EUR to UAH': 38.4188,
    'UAH to USD': 0.0271,
    'USD to UAH': 36.2664
}

# Check if the currency pair is valid
if currency_pair in exchange_rates:
    exchange_rate = exchange_rates[currency_pair]
else:
    print("Invalid currency pair. Please enter a valid source and target currency.")
    exit()

# Step 4: Perform the currency conversion and display the converted amount
converted_amount = amount * exchange_rate
print(f"{amount} {source_currency} is {converted_amount} {target_currency}")
