from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import json
import numpy as np

def matrix():
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
    return distances
def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data["distance_matrix"] = matrix()
    data["num_vehicles"] = 1
    data["depot"] = 0
    return data

def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print(f"Objective: {solution.ObjectiveValue()} miles")
    index = routing.Start(0)
    plan_output = "Route for vehicle 0:\n"
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += f" {manager.IndexToNode(index)} ->"
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += f" {manager.IndexToNode(index)}\n"
    print(plan_output)
    plan_output += f"Route distance: {route_distance}miles\n"


def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(
        len(data["distance_matrix"]), data["num_vehicles"], data["depot"]
    )

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["distance_matrix"][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(manager, routing, solution)


if __name__ == "__main__":
    main()