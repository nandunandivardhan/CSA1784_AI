import heapq

# Goal State
GOAL = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Find position of blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighboring states
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]

            # Swap blank with adjacent tile
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]

            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

# A* Search Algorithm
def solve_puzzle(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))

    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == GOAL:
            return path + [current]

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (
                        g + 1 + heuristic(neighbor),
                        g + 1,
                        neighbor,
                        path + [current]
                    )
                )

    return None

# Print solution path
def print_solution(solution):
    if solution:
        print("Solution found in", len(solution) - 1, "moves:\n")
        for step in solution:
            for row in step:
                print(row)
            print()
    else:
        print("No solution exists.")

# Example Initial State
initial_state = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

solution = solve_puzzle(initial_state)
print_solution(solution)