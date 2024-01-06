import json
 
# Opening JSON file
f = open('C:/mockHackathon/MockHackathon/Input data/level0.json')

data = json.load(f)
 
f.close()
distances = []
for i in range(data["n_neighbourhoods"]):
    distances.append(data["neighbourhoods"][f"n{i}"]["distances"])

print(distances)
restaurant = [2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323]
for i in range(len(distances)):
    j = 0
    while j < len(distances[i]):
        if distances[i][j] == 0:
            distances[i].insert(j, restaurant.pop(0))
            j += 1  # Skip the recently inserted value
        j += 1
restaurants = [0,2495, 1135, 2117, 623, 1560, 1641, 1963, 2210, 788, 1581, 1533, 1793, 1241, 510, 1765, 1442, 875, 1858, 1401, 2323]
distances.insert(0, restaurants)
print(len(distances))
print(len(distances[0]))
print(distances)
