players = {}   # žodynas, kur key = vardas, value = kitas žodynas su statistika

kiek = int(input("Kiek krepšininkų dalyvaus? "))

for i in range(kiek):
    print("\n===============================")
    vardas = input(f"{i+1}-ojo žaidėjo vardas: ")
    if vardas == "":
        vardas = f"Žaidėjas_{i+1}"