list = [1, 2.2, "Alex", "noobas"]
name = input("koks tavo vardas: ")

while True:
    print("")
    print("atspek skaiciu")
    a = int(input("irasyk skaiciu: "))
    b = 5

    if a >= b:
        print("")
        print(f"{list[2][0]} mldc {name}")
        print("")
        print("ok varom toliau ?")
        a = input("taip ar ne: ")
        x = a.lower()

        if x == "taip":
            print("ok")
        else:
            print("ot koks, nu ok")
            break   
    else:
        print(f"nera tokio {list[3]} esi {name}")
        print("")









