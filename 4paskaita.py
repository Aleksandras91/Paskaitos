print("Sveikas, pasauli!")

print(5+3)

while True:
    print(" ")

    print("SUPER skaičiuotuvas")

    user_input = input("Įrašykite pirmą skaičių (arba q, kad baigti): ")
    if user_input.lower() == "q":
        print("Programa baigta.")
        break
    num1 = float(user_input)

    mark = input("Įveskite ženklą (arba q, kad baigti): ")
    if mark == "q":
        print("Programa baigta.")
        break

    user_input = input("Įrašykite antrą skaičių (arba q, kad baigti): ")
    if user_input.lower() == "q":
        print("Programa baigta.")
        break
    num2 = float(user_input)

    if mark == "q" or num2 == "q" or num1 == "q":
        print("Programa baigta.")
        break
    
    if mark == "+":
        print(f"Suma: {num1 + num2}")
    elif mark == "-":
        print(f"Skirtumas: {num1 - num2}")
    elif mark == "*":
        print(f"Sandauga: {num1 * num2}")
    elif mark == "/":
        if mark !=0:
            print(f"Dalyba: {num1 / num2}")
        else:
            print("Klaida: dalyba iš nulio negalima.")
    elif mark == "**":
        print(f"Laipsnis: {num1 ** num2}")
    elif mark == "%":
        print(f"Liekana: {num1 % num2}")
    elif mark == "q":
        print("Programa baigta.")
        break
    else:
        print("Nežinomas ženklas.")


for x in range(10):
    print("hello, World")  
