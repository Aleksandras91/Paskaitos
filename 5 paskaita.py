counter = 1

while counter <= 10:
    print("hello, world")
    counter += 4

    # Pavyzdys paprasto begalinio ciklo, kuris be galo spausdina „Labas, Pasauli!“
while True:
    print("Labas, Pasauli!")
    # Pridėjus „break“, ciklas gali būti sustabdytas pagal tam tikras sąlygas
    response = input("Tęsti? (taip / ne): ")
    if response.lower() != "taip":
        break


list_of_cars = ["mazda", "audi", "volswagen", "audi"]

print(list_of_cars[0])

