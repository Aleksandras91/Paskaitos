# # 1
# def puzzle_pieces(a, b):
#     if len(a) != len(b):
#         return False

#     sums = []
#     for x in range(len(a)):
#         sums.append(a[x] + b[x])

#     return len(set(sums)) == 1

# print(puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]))
# print(puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]))
# print(puzzle_pieces([1, 2], [-1, -1]))
# print(puzzle_pieces([9, 8, 7], [7, 8, 9, 10]))   

# # 2
# repeat_string = (lambda text, n: text * n)
# print(repeat_string("Hello", 3)) 

# 3

def filter_restaurants(restaurants, min_reiting):
    filtered = []
    for restaur in restaurants:
        if restaur['rating'] >= min_reiting:
            filtered.append(restaur['name'])
    
    sorted_restaurants = sorted(filtered)
    return sorted_restaurants

number_of_restaurants = int(input("iveskite restoranu skaiciu: "))

restaurants = []

for x in range(number_of_restaurants):
    name = input("iveskite pavadinima: ")
    rating = int(input("iveskite reitinga: "))

    restaurants.append({'name': name, "rating": rating})

min_rating = input("ivesk reitinga ")

if min_rating == "":
    min_rating == 4
else:
    min_rating = float(min_rating)


result = filter_restaurants(restaurants, min_rating)

print(result)

