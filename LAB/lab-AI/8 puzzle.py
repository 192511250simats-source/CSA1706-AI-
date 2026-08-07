import heapq

# Goal state
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

# Find blank tile position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighboring states
def neighbors(state):
    x, y = find_blank(state)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    result = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            result.append(tuple(tuple(row) for row in new_state))
    return result

# A* Search Algorithm
def a_star(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        path = path + [current]

        if current == GOAL:
            return path

        for neighbor in neighbors(current):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (g + 1 + heuristic(neighbor), g + 1, neighbor, path)
                )

    return None

# Print puzzle state
def print_state(state):
    for row in state:
        print(row)
    print()

# Main
start = ((1, 2, 3),
         (4, 0, 6),
         (7, 5, 8))

solution = a_star(start)

if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")
    for step in solution:
        print_state(step)
else:
    print("No solution exists.")
