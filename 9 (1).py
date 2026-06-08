import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def tsp(cities):
    n = len(cities)

    tour = [0]
    unvisited = set(range(1, n))
    total = 0

    while unvisited:
        current = tour[-1]

        nearest = min(unvisited,
                      key=lambda city: distance(cities[current], cities[city]))

        total += distance(cities[current], cities[nearest])
        tour.append(nearest)
        unvisited.remove(nearest)

    total += distance(cities[tour[-1]], cities[0])
    tour.append(0)

    return tour, round(total, 2)

cities = [(0, 0), (1, 3), (4, 3), (6, 1), (3, 0)]

tour, total_distance = tsp(cities)

print("Tour:", tour)
print("Total Distance:", total_distance)