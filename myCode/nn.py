import json
import math
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

#ant colony optimization
def solve_tsp_nearest(distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    tour = []
    total_distance = 0
    
    # Start at the first city
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True
    
    
    # Repeat until all cities have been visited
    while len(tour) < num_cities:
        nearest_city = None
        nearest_distance = math.inf

        # Find the nearest unvisited city
        for city in range(num_cities):
            if not visited[city]:
                distance = distances[current_city][city]
                if distance < nearest_distance:
                    nearest_city = city
                    nearest_distance = distance

        # Move to the nearest city
        current_city = nearest_city
        tour.append(current_city)
        visited[current_city] = True
        total_distance += nearest_distance

    # Complete the tour by returning to the starting city
    tour.append(0)
    total_distance += distances[current_city][0]

    return tour, total_distance
tour, total_distance = solve_tsp_nearest(distances)

print("Tour:", tour)
print("Total distance:", total_distance)