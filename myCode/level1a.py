import json
import numpy as np
import pandas as pd


def matrix():
    f = open('C:/mockHackathon/MockHackathon/Input data/level1a.json')

    data = json.load(f)
    
    f.close()
    distances = []
    demands=[]
    for i in range(data["n_neighbourhoods"]):
        distances.append(data["neighbourhoods"][f"n{i}"]["distances"])
        demands.append(data["neighbourhoods"][f"n{i}"]["order_quantity"])
    print(distances)
    restaurant = [797,2156,563,880,521,1258, 302,2253,1829,1067, 884,1702,162,2070,1527,1719,1597,1604, 1706,390]
    for i in range(len(distances)):
        j = 0
        while j < len(distances[i]):
            if distances[i][j] == 0:
                distances[i].insert(j, restaurant.pop(0))
                j += 1  # Skip the recently inserted value
            j += 1
    restaurants = [0,797,2156,563,880,521,1258, 302,2253,1829,1067, 884,1702,162,2070,1527,1719,1597,1604, 1706,390]
    distances.insert(0, restaurants)
    demands.insert(0, 0)
    print(len(distances))
    print(len(distances[0]))
    return distances,demands

def calculate_total_distance(route, dist_matrix):
    """
    Calculate the total distance of a given route using the distance matrix.
    """
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

    while np.sum(visited) < num_points:
        current_capacity = 0
        route = []

        while current_capacity < capacity:
            start_node = None
            min_dist = float('inf')

            for node in np.where(~visited)[0]:
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
'''
paths=[]
for k in range(len(nodes_to_traverse)):
    # Use list comprehensions to extract the submatrix
    result_matrix = [[distanceMat[i][j] for j in nodes_to_traverse[k]] for i in nodes_to_traverse[k]]
    #print(result_matrix)
    tour,total_cost=tsp_nearest_neighbor_with_cost(result_matrix)
    #print(tour)
    final=[]
    for i in tour:
        if(i<n_restaurants):
            final.append('r'+str(i))
        else:
            final.append('n'+str(nodes_to_traverse[k][i]-1))
    paths.append(final)
#print(paths)'''

distance,demands = matrix()
print(len(demands))
capacity = 600
print('\n\nOptimal routes: ',nearest_neighbor(distance,demands,capacity))   

