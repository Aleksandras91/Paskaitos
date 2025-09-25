# 5 užduotis
student_gradue = {}

while True:
    name = input("Įveskite mokinio vardą (arba įveskite 'pabaiga'): ")

    if name.lower() == "pabaiga":
        break

    paz = float(input("Įveskite pažymį: "))
    student_gradue[name] = paz

if len(student_gradue) > 0:
    total = sum(student_gradue.values())
    num = len(student_gradue)
    average = (total/num)
else:
    average = 0
    print("visu vidurkis", average)

