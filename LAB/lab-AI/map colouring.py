# Map Coloring using Constraint Satisfaction Problem (CSP)

colors = ["Red", "Green", "Blue"]

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

color_assignment = {}


def is_safe(region, color):
    for neighbor in graph[region]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True


def map_coloring():
    if len(color_assignment) == len(graph):
        return True

    region = next(r for r in graph if r not in color_assignment)

    for color in colors:
        if is_safe(region, color):
            color_assignment[region] = color

            if map_coloring():
                return True

            del color_assignment[region]

    return False


if map_coloring():
    print("Map Coloring Solution:")
    for region, color in color_assignment.items():
        print(region, "->", color)
else:
    print("No solution exists")
