import json
import numpy as np
import pandas as pd


def matrix():
    f = open('C:/mockHackathon/MockHackathon/Input data/level1b.json')
    data = json.load(f)
    f.close()
    distances = []
    demands=[]
    for i in range(data["n_neighbourhoods"]):
        distances.append(data["neighbourhoods"][f"n{i}"]["distances"])
        demands.append(data["neighbourhoods"][f"n{i}"]["order_quantity"])
    print(distances)
    restaurant = data["restaurants"]["r0"]["neighbourhood_distance"]
    for i in range(len(distances)):
        j = 0
        while j < len(distances[i]):
            if distances[i][j] == 0:
                distances[i].insert(j, restaurant.pop(0))
                j += 1  # Skip the recently inserted value
            j += 1
    restaurants = restaurant.insert(0,0)
    distances.insert(0, restaurants)
    demands.insert(0, 0)
    print(len(distances))
    return distances,demands

def calculate_total_distance(route, dist_matrix):
    total_distance = 0
    num_points = len(route)

    for i in range(num_points - 1):
        current_node = route[i]
        next_node = route[i + 1]
        total_distance += dist_matrix[current_node, next_node]
    return total_distance

def nearest_neighbor(dist_matrix, demands, capacity):
    num_points = len(dist_matrix)
    visited = np.zeros(num_points, dtype=bool)
    routes = []
    print(dist[0])
    while np.sum(visited) < num_points:
        current_capacity = 0
        route = []
        print(matDis)
        while current_capacity < capacity:
            start_node = None
            min_dist = float('inf')
            print(type(dist_matrix))
            for node in np.where(~visited)[0]:
                dist_matrix[0] = matDis
                #print(dist_matrix)
                if demands[node] <= capacity - current_capacity and dist_matrix[0][node] < min_dist:
                    start_node = node
                    min_dist = dist_matrix[0][node]

            if start_node is None:
                break

            route.append(start_node)
            visited[start_node] = True
            current_capacity += demands[start_node]

            current = start_node
            while current_capacity + demands[current] <= capacity:
                nearest = None
                min_dist = float('inf')

                for neighbor in np.where(~visited)[0]:
                    print(demands)
                    if demands[neighbor] + current_capacity < capacity and dist_matrix[current][neighbor] < min_dist:
                        nearest = neighbor
                        min_dist = dist_matrix[current][neighbor]

                if nearest is None:
                    break

                route.append(nearest)
                visited[nearest] = True
                current_capacity += demands[nearest]
                current = nearest

        routes.append(route)

    return routes


distance,demands = matrix()
print(len(demands))
capacity = 1120
print(type(distance))
print('\n\nOptimal routes: ',nearest_neighbor(distance,demands,capacity))   
