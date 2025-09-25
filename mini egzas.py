print("hello world")

int(input("ivesk sveika skaiciu: "))
float(input("ivesk skaiciu per kableli: "))
input("irasyk varda: ") # str
# bool nesimokem

age = int(input("ivesk amziu: "))

if age < 18:
    print("nepilnametis")
elif age == 18:
    print("svieziai pilnametis")
else:
    print("pilnametis")


sum1 = 0
print("skaiciu seka")
for i in range(3):
    num = int(input(f"iveskite {i + 1} skaiciuka: "))
    sum1 += num

    print(f"suma: {sum1}")
      
# arba

x = 0
for x in range(5):
    print(f"{x + 1}") 


city = ["Kaunas", "Vilnius", "Klaipeda"]
print(f"{city[1]}")



dict = {"Jonas": 34, "Darius": 55, "Antanas": 20, "petras": 55 }
print(list(dict.keys())) # nezinau

for x in dict.keys():
    print(x)

a = {1, 2, 3}
b = {3, 4, 5}
print(a|b)
