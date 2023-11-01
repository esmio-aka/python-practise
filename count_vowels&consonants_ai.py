# Step 1: Prompt the user to enter a sentence
sentence = input("Enter a sentence: ").casefold()

# Step 2: Initialize counters for vowels and consonants
vowels_count = 0
consonants_count = 0

# Step 3: Use a 'for' loop to iterate over the characters in the sentence
for char in sentence:
    if char.isalpha():  # Check if the character is an alphabet letter
        if char in 'aeiou':  # Check if the character is a vowel
            vowels_count += 1
        else:
            consonants_count += 1

# Step 4: Display the count of vowels and consonants
print(f'Vowels: {vowels_count}')
print(f'Consonants: {consonants_count}')
