

def belenkoks_trumpas_kodo_pavadinimas(): #naudojamas kai daug eiluciu kodo
    print("")

belenkoks_trumpas_kodo_pavadinimas() #funkc iškvietimas

belenkoks_trumpas_kodo_pavadinimas() # left ctrl ir kaire pelyte, tiesiai ant to kodo keliauja


def division(num1, num2):
    return num1 / num2

print(division(6, 2))
print(division(num1=3, num2=3))
print(division(num1=4, num2=2))
print(division(3, num2=3))
# print(division(num1=3, 3)) negalima

def multiplication(num1=1, num2=2):
    return num1 * num2

print(multiplication(1, 2))
print(multiplication(3, 3))
print(multiplication(3))
print(multiplication())
print(multiplication(num1=6, num2=9))
print(multiplication(6, num2=9))
# multiplication(num1=6, 9) negalima

print("labas", "vakaras", sep=" ")
print("labas", "vakaras", sep=" ")
print("labas", end="****")
print("labas", end="****")
print("labas", end="****")

a = "kas yra "
b = 1
print(type(b)) #paaiskina koks tipas
print(len(a)) #isspauzdina raidziu kieki


c = 1.88954
print(round(c))
print(round(c, ndigits=4)) #jei nurodai ndigits=2 → apvalina iki dviejų skaičių po kablelio.

d = [2, 1, 6, 9, 10, 1, 5000, 0]
e = {2, 1, 6, 9, 10, 1, 5000, 0}
print(sorted("labas"))
print(sorted([5, 9, 7, 5, 2, 1]))
print(sorted([5, 9, 7, 5, 2, 1], reverse=True))
print(sorted([d]))
print(sorted([d], reverse=True))
print(sorted(d))
print(sorted(d, reverse=True))
print(sorted([e]))
print(sorted([e], reverse=True))

def print_greeting(full_name: str):
    name = full_name.split(" ")[0]
    print(f"Hello {name}")

full_name = " Aleksandras"
name: str = "Aleksandras"

print(print_greeting())