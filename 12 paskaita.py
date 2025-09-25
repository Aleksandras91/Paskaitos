squares = []

for number in range(1, 11):
    squares.append(number * number)

print(squares)


squares = [number for number in range(1, 11)]
print(squares)


squares_even = [number for number in range(1, 11) if number % 2 == 0]
print(squares_even)


squares_even1 = []

for number in range(1, 11):
    if number % 2 == 0:
        squares_even1.append(number)
print(squares_even1)


names = ["jonas", "Antanas", "Aleksandras", "lapas"]
names_start_with_a = {names for names in names if names.startswith("A") or "l" in names}
print(names_start_with_a)

names = ["jonas", "Antanas", "Aleksandras", "lapas"]
names_start_with_a = [names for names in names if names.startswith("A") or "l" in names]
print(names_start_with_a)

names = ["jonas", "Antanas", "Aleksandras", "lapas"]
names_start_with_a = [name for name in names if name.startswith("A") or "l" in name]
for x in names_start_with_a:
    print(x)

squares2 = {number: number * number for number in range(1, 11)}
print(squares2)

values = ["a", "b", "c", "d"]
index = 1

for value in values:
    print(f"{index}: {value}")
    index = index + 1 

values = ["a", "b", "c", "d"]

for index, value in enumerate(values, start=1):
    print(f"{index}: {value}")



import math

area = 5 * 5 * math.pi

print(area)

print(math.factorial(7))

print(math.ceil(5.12))

print(math.floor(5.12))

print(math.pow(5, 6))

print(math.sqrt(25))

