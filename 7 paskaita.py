# 2 užduotis

stud_list = set()

while True:
    stud = input("Įveskite mokinio vardą (arba įveskite 'pabaiga'):")
    if stud.lower() == "pabaiga":
        break
    stud_list.add(stud)
    print(f"šaunu {stud}, jus pridėtas prie sąrašo")

while True:
    print("Ar norite sužinoti kas vyksta į kelionę: ")
    list = input("Įrašykite taip/ne: ").lower

    if list == "ne":
        print("ok, kaip nori")
        break
    elif list == "taip":
        print("Mokinių, kurie vyksta į kelionę, sąrašas:", stud_list)
        break
    else:
        print("nesupratau")


# 3 užduotis

dictionary = {
    "obuolys": "vaisius, augantis ant medžių",
    "knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius",
    "kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",
}


while True:
    word = input("Įveskite žodį, kad sužinotumėte jo reikšmę (arba 'pabaiga'): ").lower

    if word == "pabaiga":
        break

    if word in dictionary:
        print(f"žodžio {word} reikšmė yra: {dictionary[word]}")
    else:
        print("tokio žodžio nėra")
        


