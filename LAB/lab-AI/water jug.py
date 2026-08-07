from collections import deque

def water_jug():
    # Capacities of the jugs
    A = 4
    B = 3

    # Starting state
    start = (0, 0)

    # Goal: 2 gallons in Jug A
    goal = 2

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        # Add current state to path
        path = path + [(a, b)]

        # Goal check
        if a == goal:
            print("Solution found:\n")
            for state in path:
                print("Jug A =", state[0], " Jug B =", state[1])
            return

        # Possible operations
        states = []

        # 1. Fill Jug A
        states.append((A, b))

        # 2. Fill Jug B
        states.append((a, B))

        # 3. Empty Jug A
        states.append((0, b))

        # 4. Empty Jug B
        states.append((a, 0))

        # 5. Pour A -> B
        transfer = min(a, B - b)
        states.append((a - transfer, b + transfer))

        # 6. Pour B -> A
        transfer = min(b, A - a)
        states.append((a + transfer, b - transfer))

        # Add new states to queue
        for state in states:
            if state not in visited:
                queue.append((state, path))


water_jug()
