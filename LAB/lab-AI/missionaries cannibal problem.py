from collections import deque

# State: (missionaries_left, cannibals_left, boat_position)
# boat_position: 0 = Left, 1 = Right

def is_valid(state):
    m_left, c_left, boat = state

    m_right = 3 - m_left
    c_right = 3 - c_left

    # Check valid range
    if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False

    # Check left side
    if m_left > 0 and c_left > m_left:
        return False

    # Check right side
    if m_right > 0 and c_right > m_right:
        return False

    return True


def get_next_states(state):
    m_left, c_left, boat = state

    # Possible boat movements
    moves = [
        (1, 0),  # 1 missionary
        (2, 0),  # 2 missionaries
        (0, 1),  # 1 cannibal
        (0, 2),  # 2 cannibals
        (1, 1)   # 1 missionary and 1 cannibal
    ]

    next_states = []

    for m, c in moves:

        if boat == 0:  # Boat moves Left -> Right
            new_state = (m_left - m, c_left - c, 1)
        else:          # Boat moves Right -> Left
            new_state = (m_left + m, c_left + c, 0)

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states


def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque()
    queue.append((start, [start]))

    visited = set()
    visited.add(start)

    while queue:
        state, path = queue.popleft()

        # Goal reached
        if state == goal:
            print("Solution Found:\n")

            for i, s in enumerate(path):
                m, c, boat = s

                side = "Left" if boat == 0 else "Right"

                print(
                    "Step", i,
                    ": Missionaries =", m,
                    "Cannibals =", c,
                    "Boat =", side
                )

            return

        # Generate next states
        for next_state in get_next_states(state):

            if next_state not in visited:
                visited.add(next_state)
                queue.append(
                    (next_state, path + [next_state])
                )

    print("No solution found.")


solve()
