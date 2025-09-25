# Vartotojas turi pasirinkti, kiek krepšininkų dalyvaus (pvz., 2, 3 ar daugiau).
# Kiekvienam krepšininkui vartotojas turi įvesti jo vardą.

players = {}

zaideju_skaic = int(input("kiek krepšininkų dalyvaus? "))

# statistika. šiaip galima ir while true kartu su break:
for x in range(zaideju_skaic):
    print(" ")
    name = input(f"{x+1} Įveskite žaidėjo vardą: ")
   
    baud_mesta = int(input("kiek metė baudų: "))
    baud_pataikyta = int(input("kiek pataikė baudų: "))
    dvit_mesta = int(input("kiek metė dvitaškių: "))
    dvit_pataikyta = int(input("kiek pataikė dvitaškių: "))
    trit_mesta = int(input("kiek metė tritaškių: "))
    trit_pataikyta = int(input("kiek pataikė tritaškių: "))

#Skaičiavimai
    points = baud_pataikyta*1 + dvit_pataikyta*2 + trit_pataikyta*3
    visi_mesti = baud_mesta + dvit_mesta + trit_mesta
    pataikyti_metimai = baud_pataikyta + dvit_pataikyta + trit_pataikyta

    if visi_mesti > 0:
        taiklumas = pataikyti_metimai / visi_mesti * 100
    else:
        taiklumas = 0

    zaidimo_mesta = dvit_mesta + trit_mesta
    zaidimo_pataikyta = dvit_pataikyta + trit_pataikyta
    if zaidimo_mesta > 0:
        zaidimo_taiklumas = zaidimo_pataikyta / zaidimo_mesta * 100
    else:
        zaidimo_taiklumas = 0

    players[name] = {
        "baudų_mesta": baud_mesta,
        "pataikė baudų": baud_pataikyta,
        "dvitaškių mesta": dvit_mesta,
        "dvitaškių pataikyta": dvit_pataikyta,
        "tritaškių mesta": trit_mesta,
        "tritaškių pataikyta": trit_pataikyta,
        "viso taškų": points,
        "taiklumas": taiklumas,
        "žaidimo mesta": zaidimo_mesta,
        "žaidimo taiklumas": zaidimo_taiklumas
    }

print("")
# 1 rezultatas, atspauzdinti sąrašą su žaidėjais, taškais ir taiklumu
print("Rezultatai: ")

for name in players:
    print(f"{name, {players[name]['viso taškų']}, points, {players[name]['taiklumas']}, taiklumas}")

# 2 rezultatas
# Programos  pabaigoje programėlė turi paskelbti, kuris krepšininkas buvo rezultatyviausias). Jei keli vienodai – tada žiūrėti, kuris krepšininkas taiklesnis. 
rezultatyviausias = 0
max_taskai = 0
max_taiklumas = 0

for name in players:
    if players[name]["viso taškų"] > max_taskai or (players[name]["viso taškų"] == max_taskai and players[name]["taiklumas"] > max_taiklumas):
        
        rezultatyviausias = name
        max_taskai = players[name]["viso taškų"]
        max_taiklumas = players[name]["taiklumas"]
print("")
print("Rezultatyviausias yra: ")
print(rezultatyviausias, "-", max_taskai, "taškų,", "taiklumas", round(max_taiklumas,1), "%")

# 3 rezultatas
taikliausias_is_zaidimo = 0
max_zaidimo_taiklumas = 0

for name in players:
    mestas = players[name]["žaidimo mesta"]
    taik = players[name]["žaidimo taiklumas"]
    if mestas >= 3:
        if taik > max_zaidimo_taiklumas:
            taikliausias_is_zaidimo = name
            max_zaidimo_taiklumas = taik
print("")
if taikliausias_is_zaidimo == " ":
    print("nėra tinkamų (niekas nemetė ≥ 3 metimų).")
else:
    print("Taikliausias iš žaidimo:")
    print(f"{taikliausias_is_zaidimo} - taiklumas, {max_zaidimo_taiklumas} %",'mesta:', players[taikliausias_is_zaidimo]["žaidimo mesta"],"kartus")

# 4 rezultatas

taikliausias_is_baudu = 0
best_pct = 0
best_mesta = 0

for vardas in players:
    mesta = players[vardas]["baudų_mesta"]
    pataikyta = players[vardas]["pataikė baudų"]

    if mesta > 0:
        pct = pataikyta / mesta * 100 
    else:
        pct = 0

    players[vardas]["baudų taiklumas"] = pct
    
    if (pct > best_pct) or (pct == best_pct and mesta > best_mesta):
        taikliausias_is_baudu = vardas
        best_pct = pct
        best_mesta = mesta
print("")
if taikliausias_is_baudu == " ":
    print("\nniekas nemetė baudų.")
else:
    print("Taikliausias iš baudų:")
    print(f"{taikliausias_is_baudu} - taiklumas, {best_pct}%", '(mesta:', best_mesta, 'kartus)')






