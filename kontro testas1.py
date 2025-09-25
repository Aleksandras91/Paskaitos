player_count = int(input("Iveskite krepsininku kieki: "))

players = [] 

for i in range(player_count):
    print("Zaidejas nr. ", i+1)
    name = input("Vardas: ")

    one_point = int(input("Baudos metimai - mesti: "))
    if one_point > 0: 
        one_point_hit = int(input("Baudos metimai - pataikyti: "))
    else:
        one_point_hit = 0

    two_point = int(input("Dvitaskiai - mesti: "))
    if two_point > 0: 
        two_point_hit = int(input("Dvitaskiai - pataikyti: "))
    else:
        two_point_hit = 0

    three_point = int(input("Tritaskiai - mesti: "))
    if three_point > 0: 
        three_point_hit = int(input("Tritaskiai - pataikyti: "))
    else:
        three_point_hit = 0

    total_points = one_point_hit * 1 + two_point_hit * 2 + three_point_hit * 3
    total_shots = one_point + two_point + three_point
    total_hits = one_point_hit + two_point_hit + three_point_hit
    accuracy = (total_hits/total_shots * 100) if total_shots > 0 else 0
    free_throw_accuracy = (one_point_hit/one_point * 100) if one_point > 0 else 0

    players.append({
        "name": name,
        "total_points": total_points,
        "total_shots": total_shots,
        "total_hits": total_hits,
        "accuracy": accuracy,
        "free_throw_accuracy": free_throw_accuracy,
        "free_throw_shots": one_point
    })

print(players)

max_points = 0 
top_player = None
for p in players: 
    if p["total_points"] > max_points: 
        max_points = p['total_points'] # Mantas
        max_accuracy = p["accuracy"] # 75
        top_player = p
    elif p["total_points"] == max_points and p["accuracy"] > max_accuracy:
        max_accuracy = p["accuracy"]
        top_player = p

print(top_player)
print(f"\nRezultatyviausias žaidėjas: {top_player['name']} ({top_player['total_points']} taškai, taiklumas {top_player['accuracy']:.2f}%)")

if len(players) > 0:
    max_game_accuracy = 0
    for p in players:
        if p["accuracy"] > max_game_accuracy:
            max_game_accuracy = p["accuracy"]

    best_game_players = []
    for p in players:
        if p["accuracy"] == max_game_accuracy:
            best_game_players.append(p)

    best_game_player = best_game_players[0]
    max_shots = best_game_player["total_shots"]
    for p in best_game_players:
        if p["total_shots"] > max_shots and p["total_shots"] > 3:
            best_game_player = p
            max_shots = p["total_shots"]

    print(f"Taikliausias žaidėjas iš žaidimo: {best_game_player['name']} ({best_game_player['accuracy']:.2f}%, metė {best_game_player['total_shots']} kartus)")

if len(players) > 0:
    max_game_free_throw = 0
    for p in players:
        if p["free_throw_accuracy"] > max_game_free_throw:
            max_game_free_throw = p["free_throw_accuracy"]

    best_free_throw_players = []
    for p in players:
        if p["free_throw_accuracy"] == max_game_free_throw:
            best_free_throw_players.append(p)

    best_free_throw_player = best_free_throw_players[0]
    max_shots = best_game_player["free_throw_shots"]
    for p in best_free_throw_players:
        if p["free_throw_shots"] > max_shots and p["free_throw_shots"] > 3:
            best_free_throw_player = p
            max_shots = p["free_throw_shots"]

    print(f"Taikliausias žaidėjas iš baudų linijos: {best_free_throw_player['name']} ({best_free_throw_player['free_throw_accuracy']:.2f}%, metė {best_free_throw_player['free_throw_shots']} kartus)")
 