num = [1, 2, 3, 5, 100, 2000, 5000, -550, -5]

biggest = max(num)
print(biggest)

smallest = min(num)
print(smallest)

skaic = len(num)
print(skaic)

name = "Simkaaaa"

for x in name:
    print(x)



names = ["alex", "dovys", "tomas", "vilija", "simka"]

nam = input("ivesk varda: ")
namy = nam.lower()

if namy in names:
    print(f"esi, sveikinu tave {namy}")
else:
    print("taves nera :D")
    
sar = input("nori saraso? irasyk taip: ")    
sar1 = sar.lower()

if sar1 == "taip":
    for x in names:
        print(x)
else:
    print("kaip nori")



