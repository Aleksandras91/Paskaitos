# 2 užduotis

stud_list = set()

while True:
    print(" ")
    stud = input("Įveskite mokinio vardą (arba įveskite 'pabaiga'):").lower()
    if stud == "pabaiga":
        break
    stud_list.add(stud)
    print(f"šaunu {stud.capitalize()}, jus pridėtas prie sąrašo")

while True:
    print("Ar norite sužinoti kas vyksta į kelionę:")
    list = input("Įrašykite taip/ne: ")
    if list.lower() == "ne":
        print("ok, kaip nori")
        break
    elif list == "taip":
        print(f"Mokinių, kurie vyksta į kelionę, sąrašas: ", stud_list)
        break



# 3 užduotis

dictionary = {
    "obuolys": "vaisius, augantis ant medžių",
    "knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius",
    "kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",
}


while True:
    print(" ")
    word = input("Įveskite žodį, kad sužinotumėte jo reikšmę (arba 'pabaiga'): ").lower()

    if word == "pabaiga":
        break
    if word in dictionary:
        print(f"žodžio {word} reikšmė yra: {dictionary[word]}")
    else:
        print("tokio žodžio nėra")
        



# 5 užduotis
student = {}

while True:
    name = input("Įveskite mokinio vardą (arba įveskite 'pabaiga'): ").lower()
    if name == "pabaiga":
        break
    paz = float(input("Įveskite pažymį: "))

    student[name] = paz

if len(student) > 0:
    total_paz = sum(student.values())
    total_name = len(student)
    average = total_paz / total_name 
else :
    average = 0
print(f"visu vidurkis")


