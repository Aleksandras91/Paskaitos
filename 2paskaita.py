
print("pirma uzduotis:")

# Parašykite Python programą, kuri gauna du skaičius iš vartotojo, sudeda juos ir atspausdina rezultatą. Prieš atliekant sudėtį, būtinai konvertuokite įvestis į sveikuosius skaičius.
# Įveskite pirmą skaičių: 5
# Įveskite antrą skaičių: 3
# Suma yra 8
a = int(input("irasykite skaiciu:"))
b = int(input("irasykite skaiciu:"))
result = a+b

print("suma:", result)

print("antra uzduotis:")

# Parašykite programą, kuri prašo vartotojo įvesti temperatūrą pagal Farenheitą, konvertuoja ją į Celsijaus laipsnius ir atspausdina rezultatą. Konvertavimo formulė yra C = (F−32) × 5/9​.
# Įveskite temperatūrą pagal Farenheitą: 68
# Temperatūra pagal Celsijų: 20.0

tempF = float(input("irasykite temperatura pagal F: "))

print((tempF-32)*5/9, "celsiju")


print("trecia uzduotis:")

# Parašykite programą, kuri gauna iš vartotojo vieną žodį, apverčia simbolių tvarką ir atspausdina rezultatą.
# Įveskite žodį: hello
# Apverstas žodis: olleh

word = input("iveskite zodi: ")
zodis = (word)
reversed = zodis[::-1]

print("apverstas zodis: ", reversed)

print("4 uzduotis:")

# Sukurkite programą, kuri prašo vartotojo atskirai įvesti savo vardą ir pavardę, o tada atspausdina juos oficialiai – pirmiausia pavardė, po jos kablelis, tarpas, ir tada – vardas.
# Įveskite savo vardą: John
# Įveskite savo pavardę: Doe
# Formatuotas vardas: Doe, John

first_name = input("iveskite varda: ")
last_name = input("iveskite pavarde: ")
formatuotas = f"{last_name}, {first_name}"

print("oficialiai esi: ", formatuotas)

print("5 uzduotis:")

# Parašykite programą, kuri prašo vartotojo įvesti pradinę sumą, metinę palūkanų normą (procentais) ir laiką (metų skaičių). Apskaičiuokite paprastąsias palūkanas naudodami formulę PP=(P×N×L)/100 ir atspausdinkite rezultatą.
# Įveskite pradinę sumą: 1000
# Įveskite palūkanų normą (%): 5
# Įveskite laiką (metais): 3
# Paprastosios palūkanos yra 150.0

P = float(input("Įveskite pradinę sumą: "))
N = float(input("Įveskite palūkanų normą (%): "))
L = float(input("Įveskite laiką (metais): "))
PP = (P * N * L) / 100

print("Paprastosios palūkanos yra", PP)

print("6 uzduotis:")

# Parašykite programą, kuri paima vartotojo vardą iš jo įvesto pilno vardo ir sukuria asmeninį pasveikinimą. Pilnas vardas įvedamas formatu „Vardas Pavardė“. Pasveikinime vardas turi būti užrašytas visomis didžiosiomis raidėmis.
# Įveskite savo pilną vardą: Jonas Jonaitis
# Labas, JONAS, sveiki atvykę!

full_name = input("iveskite varda: ")
first_name = full_name.split(" ")[0] 
greeting = f"Labas, {first_name}, sveikas atvykes!"

print(greeting)

