goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                h += 1
    return h


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def neighbors(state):
    x, y = find_blank(state)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = []

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]

            # Swap blank with adjacent tile
            new_state[x][y], new_state[nx][ny] = (
                new_state[nx][ny],
                new_state[x][y]
            )

            result.append(new_state)

    return result

def a_star(start):
    open_list = [start]
    closed_list = []

    while open_list:
        # Select state with minimum heuristic value
        current = min(open_list, key=heuristic)
        open_list.remove(current)

        if current == goal:
            print("Goal Reached!")
            for row in current:
                print(row)
            return

        closed_list.append(current)

        for neighbor in neighbors(current):
            if neighbor not in open_list and neighbor not in closed_list:
                open_list.append(neighbor)

    print("No Solution Found")

# Driver Code
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

a_star(start)

