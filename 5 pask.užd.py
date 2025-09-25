username1 = "admin"
password1 = "123"

while True:
    username = input("Įveskite vardą: ")
    password = input("Įveskite slaptažodį: ")
    
    if username == username1 and password == password1:
        print(f"Sveikas atvykęs, {username}.")
        break
    else:
        print("bandyk dar karta noobas")
        

sum = 0

for i in range(10):
    num = int(input(f"iveskite {i + 1} skaiciuka: "))
    sum += num

print("suma", sum)

