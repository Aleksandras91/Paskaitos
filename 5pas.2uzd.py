sum = 0

for x in range(10):
    num = int(input(f"iveskite {x + 1} skaiciuka: "))
    sum += num

print(f"suma: {sum}, o vidurkis:", sum/10)


pin = "1234"

for x in range(10000):
    pinas = str(x)
    while len(pinas) < 4:
        pinas = "0" + pinas

    if pinas == pin:
        print(f"pinas surastas: {pinas}")
        break