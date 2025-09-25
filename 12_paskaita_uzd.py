# Skaičiai nuo 1 iki 1000, kurie dalijasi iš 6: [6, 12, 18, ..., 996]

squares_even1 = []

for number in range(1, 1000):
    if number % 6 == 0:
        squares_even1.append(number)

print("skaiciai kurie dalinasi is 6 yra: ", squares_even1)
print("")
# Skaičiai nuo 1 iki 1000, kuriuose yra 9: [9, 19, 29, ..., 999]
numbers_with9 = [sk for sk in range(1, 1000) if "9" in str(sk)]
print("skaiciai kur yra 9 yra: ", numbers_with9)

# Įveskite tekstą: Šioje paskaitoje aptarsime papildomas Python integruotų duomenų struktūrų funkcijas.
# Žodžių su 'e' skaičius: 5


text = input("iveskite teksta: ")
words = text.split()
count = 0

for word in words:
    if "e" in word:
        count += 1

        print(f"{word} is viso e raidziu yra: {word.count("e")}")
print(count)



def count_long_words(text):
    return len([word for word in text.split() if len(word) > 5])

# Įveskite tekstą: Šioje paskaitoje aptarsime papildomas Python integruotų duomenų struktūrų funkcijas.
# Žodžių, ilgesnių nei penki simboliai, skaičius: 8

user_text = input("Įveskite tekstą: ")
long_words_count = count_long_words(user_text)
print("Žodžių, ilgesnių nei penki simboliai, skaičius:", long_words_count)