# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:34:48 2023

@author: julia
"""

graph = {
    'Atlanta': {'Charleston': 2, 'Miami': 5, 'Nashville': 1, 'New Orleans': 4, 'Raleigh': 2},
    'Boston': {'Montreal': 2, 'New York': 2},
    'Calgary': {'Helena': 4, 'Seattle': 4, 'Vancouver': 3, 'Winnipeg': 6},
    'Charleston': {'Atlanta': 2, 'Miami': 4, 'Raleigh': 2},
    'Chicago': {'Duluth': 3, 'Omaha': 4, 'Pittsburgh': 3, 'Saint Louis': 2, 'Toronto': 4},
    'Dallas': {'El Paso': 4, 'Houston': 1, 'Little Rock': 2, 'Oklahoma City': 2},
    'Denver': {'Helena': 4, 'Kansas City': 4, 'Oklahoma City': 4, 'Phoenix': 5, 'Salt Lake City': 3, 'Santa Fe': 2},
    'Duluth': {'Chicago': 3, 'Helena': 6, 'Kansas City': 5, 'Omaha': 2, 'Sault St. Marie': 3, 'Toronto': 6, 'Winnipeg': 4},
    'El Paso': {'Dallas': 4, 'Houston': 6, 'Los Angeles': 6, 'Oklahoma City': 5, 'Phoenix': 3, 'Santa Fe': 2},
    'Helena': {'Calgary': 4, 'Denver': 4, 'Duluth': 6, 'Omaha': 5, 'Salt Lake City': 3, 'Seattle': 6, 'Winnipeg': 4},
    'Houston': {'Dallas': 1, 'El Paso': 6, 'New Orleans': 2},
    'Kansas City': {'Denver': 4, 'Duluth': 5, 'Omaha': 1, 'Oklahoma City': 2, 'Saint Louis': 2},
    'Las Vegas': {'Los Angeles': 2, 'Salt Lake City': 3},
    'Little Rock': {'Dallas': 2, 'Nashville': 3, 'New Orleans': 3, 'Oklahoma City': 2, 'Saint Louis': 2},
    'Los Angeles': {'El Paso': 6, 'Las Vegas': 2, 'Phoenix': 3, 'San Francisco': 3},
    'Miami': {'Atlanta': 5, 'Charleston': 4, 'New Orleans': 6},
    'Montreal': {'Boston': 2, 'New York': 3, 'Sault St. Marie': 5, 'Toronto': 3},
    'Nashville': {'Atlanta': 1, 'Little Rock': 3, 'Pittsburgh': 4, 'Raleigh': 3, 'Saint Louis': 2},
    'New Orleans': {'Atlanta': 4, 'Houston': 2, 'Little Rock': 3, 'Miami': 6},
    'New York': {'Boston': 2, 'Montreal': 3, 'Pittsburgh': 2, 'Washington': 2},
    'Oklahoma City': {'Dallas': 2, 'Denver': 4, 'El Paso': 5, 'Kansas City': 2, 'Little Rock': 2},
    'Omaha': {'Chicago': 4, 'Denver': 4, 'Duluth': 2, 'Helena': 5, 'Kansas City': 1},
    'Phoenix': {'Denver': 5, 'El Paso': 3, 'Los Angeles': 3, 'Santa Fe': 3},
    'Pittsburgh': {'Chicago': 3, 'Nashville': 4, 'New York': 2, 'Raleigh': 2, 'Saint Louis': 5, 'Toronto': 2, 'Washington': 2},
    'Portland': {'Salt Lake City': 6, 'San Francisco': 5, 'Seattle': 1},
    'Raleigh': {'Atlanta': 2, 'Charleston': 2, 'Nashville': 3, 'Pittsburgh': 2, 'Washington': 2},
    'Saint Louis': {'Chicago': 2, 'Kansas City': 2, 'Little Rock': 2, 'Nashville': 2, 'Pittsburgh': 5},
    'Salt Lake City': {'Denver': 3, 'Helena': 3, 'Las Vegas': 3, 'Portland': 6, 'San Francisco': 5},
    'San Francisco': {'Los Angeles': 3, 'Portland': 5, 'Salt Lake City': 5},
    'Santa Fe': {'Denver': 2, 'El Paso': 2, 'Phoenix': 3},
    'Seattle': {'Calgary': 4, 'Helena': 6, 'Portland': 1, 'Vancouver': 1},
    'Sault St. Marie': {'Duluth': 3, 'Montreal': 5, 'Toronto': 2, 'Winnipeg': 6},
    'Toronto': {'Chicago': 4, 'Duluth': 6, 'Montreal': 3, 'Pittsburgh': 2, 'Sault St. Marie': 2},
    'Vancouver': {'Calgary': 3, 'Seattle': 1},
    'Washington': {'New York': 2, 'Pittsburgh': 2, 'Raleigh': 2},
    'Winnipeg': {'Calgary': 6, 'Duluth': 4, 'Helena': 4, 'Sault St. Marie': 6}
}
def score_route(trains):
    if trains == 1:
        return 1
    elif trains == 2:
        return 2
    elif trains == 3:
        return 4
    elif trains == 4:
        return 7
    elif trains == 5:
        return 10
    elif trains == 6:
        return 15
    else:
        return 0

def depth_limited_search(graph, target_cities, max_trains, depth_limit):
    best_path, best_score, total_trains_used = None, float('-inf'), 0

    def dfs(current_city, visited, score, remaining_targets, trains_used, depth):
        nonlocal best_path, best_score, total_trains_used

        if not remaining_targets:
            if score > best_score:
                best_path, best_score, total_trains_used = visited, score, trains_used
            return

        if depth == depth_limit:
            return

        for neighbor, route_trains in graph[current_city].items():
            if neighbor not in [city for city, _ in visited] and trains_used + route_trains <= max_trains:
                new_visited = visited + [(current_city, neighbor)]
                new_remaining_targets = remaining_targets - set([neighbor]) if neighbor in remaining_targets else remaining_targets
                route_score = score_route(route_trains)
                new_score = score + route_score
                dfs(neighbor, new_visited, new_score, new_remaining_targets, trains_used + route_trains, depth + 1)

    for city in graph.keys():
        dfs(city, [], 0, target_cities, 0, 0)

    return best_path, best_score, total_trains_used

def iterative_deepening_search(graph, target_cities, max_trains):
    target_cities = set(target_cities)  # Convert target_cities to a set
    depth_limit = 1
    best_path, best_score, total_trains_used = None, float('-inf'), 0

    while best_score == float('-inf'):
        path, score, trains_used = depth_limited_search(graph, target_cities, max_trains, depth_limit)
        if score > best_score:
            best_path, best_score, total_trains_used = path, score, trains_used
        depth_limit += 1

    return best_path, best_score, total_trains_used