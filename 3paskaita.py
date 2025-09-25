a = float(input("Įveskite pirmą skaičių: "))
b = float(input("Įveskite antrą skaičių: "))

if a > b:
    print("Didesnis skaičius yra", a)
elif a < b:
    print("Didesnis skaičius yra", b)
else:
    print("Abu skaičiai yra lygūs.")


first_name = input("iveskite savo varda: ")
last_name = input("iveskite savo pavarde: ")
age = input("iveskite savo amziu: ")


statusas = input("Ar esate bibliotekos narys? (taip / ne): ").lower()

if statusas == "taip":
    age = int(input("Įveskite savo amžių: "))
    if age >= 12:
        print("Jūs galite skolintis visas knygas.")
    else:
        tevai = input("Ar jus lydi suaugęs asmuo? (taip / ne): ").lower()
        if tevai == "taip":
            print("Jūs galite skolintis visas knygas.")
        else:
            print("Jūs galite skolintis tik vaikų knygas.")
else:
    print("Jūs negalite skolintis jokių knygų.")



numa = float(input("Įveskite pirmą skaičių: "))
b = input("Įveskite simbolį (+, -, *, /): ")
numb = float(input("Įveskite antrą skaičių: "))
result = None
 
if b == "*":
    result = numa * numb
elif b == "+":
    result = numa + numb
elif b == "-":
    result = numa - numb
elif b == "/":
    result = numa / numb
   
    print(f"{numa} {b} {numb} rezultatas yra {result}")


# Atspėkite skaičių (1–10): 5
# Per mažas! Bandykite dar kartą.
# Atspėkite skaičių (1–10): 8
# Teisingai! Skaičius yra 8.

import random
n = random.randrange(1,10)
guess = float(input("Enter any number: "))
while n == guess:
    if guess < n:
        print("Too low")
        guess = float(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = float(input("Enter number again: "))
    else:
      break
print("you guessed it right!!")





