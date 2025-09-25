# def pasisveikinti():
#     print("Sveikas, pasauli!")

# pasisveikinti()
# pasisveikinti()
# pasisveikinti()

# for x in range(5):
#     print(f"{x}", "labas")


# def daug_kvadratu(*args):
#     for skaicius in args:
#         print(skaicius ** 2)


# daug_kvadratu(4, 5, 7, 8, 9, 10)

# def spausdinti_reiksmes(**kwargs):
#     for raktas, reiksme in kwargs.items():
#         print(raktas, reiksme)


# spausdinti_reiksmes(vardas="Tomas", pavarde="Rutkauskas", lytis="Vyras", amzius=29, daiktai=["Telefonas", "Ausinės", "Krepšys"])

# # vardas Tomas
# # pavarde Rutkauskas
# # lytis Vyras
# # amzius 29
# # daiktai ['Telefonas', 'Ausinės', 'Krepšys']


# globalus = 10

# def funkcija():
#     lokalus = 12
#     suma = globalus + lokalus
#     print(suma)

#     kita_suma = globalus + lokalus
#     print(kita_suma)
# # NameError: name 'lokalus' is not defined

# funkcija()
# # 22

# def funkcija(parametras1, parametras2):
#     '''
    
#     :param parametras1:
#     :param parametras2:
#     :return:
#     '''
#     return

def sum_of_three(first,second,third):
    return first + second + third

def sum_of_list(list_of_something):
    x = 0
    for element in list_of_something:
        x+=element

    return x


print(sum_of_three(2,2,5))
print(sum_of_list([4,3,1,10]))

print("3: Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).")
def max_of_numbers(*args):
    return max(args)

print(max_of_numbers(4, 3, 1, 10))

print("4: Gražintų paduotą stringą atbulai.")

def reverse(textas):
    return textas[::-1]

print(reverse("Aleksandras"))

print("5 Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.")

def analyze_words(textas1):
    words = len(textas1.split())
    upper = 0
    lower = 0
    digits = 0

    for c in textas1:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digits += 1

    return words, upper, lower, digits


sentence = "Laba diena, aš esu Aleksandras 2025"
w, u, l, d = analyze_words(sentence)

print("Žodžių:", w)
print("Didžiųjų raidžių:", u)
print("Mažųjų raidžių:", l)
print("Skaičių:", d)


print("6: ")

def unique_list(lst):
    return list(set(lst))

print(unique_list([1, 2, 3, 5, 9, 11]))


# 7 Gražintų, ar paduotas skaičius yra pirminis.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))

# 8 Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo

def reverse_words(text):
    words = text.split()
    return (words[::-1])

print(reverse_words("Laba diena aš esu Aleksandras"))

# 9 Ar metai keliamieji

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

print(is_leap_year(2024))
print(is_leap_year(2025))

# 10 Kiek nuo sukakties praėjo laiko

from datetime import datetime

def time_since(date_string):
    event_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    diff = now - event_date

    years = diff.days // 365
    months = (diff.days % 365) // 30
    days = (diff.days % 365) % 30
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60

    return years, months, days, hours, minutes, seconds


print(time_since("1991-02-01 07:00:00"))





