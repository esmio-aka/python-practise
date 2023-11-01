raw_sentense = input("Enter a sentense (e.g. \"I love Python\"): ").casefold()
vowels_list = ('a', 'e', 'i', 'o', 'u')
sentense = [char for char in raw_sentense if char.isalpha()]
vowels_count = 0
cons_count = 0
if sentense:
    for i in sentense:
        if i in vowels_list:
            vowels_count += 1
        elif i not in vowels_list:
            cons_count +=1

    print(f'{vowels_count} vowels')
    print(f'{cons_count} consonants')

else:
    print('Nothing to count')

