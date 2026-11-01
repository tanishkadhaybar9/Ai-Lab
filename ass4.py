from collections import deque

def moves(state):
    result = []

    for i in range(3):
        if not state[i]:
            continue

        disk = state[i][-1]

        for j in range(3):
            if i != j and (not state[j] or state[j][-1] > disk):
                new = [list(p) for p in state]
                new[i].pop()
                new[j].append(disk)
                result.append(tuple(tuple(p) for p in new))

    return result

start = ((3, 2, 1), (), ())
goal = ((), (), (3, 2, 1))

queue = deque([(start, [])])
visited = {start}

while queue:
    state, path = queue.popleft()

    if state == goal:
        print("Solution:")
        for step in path + [state]:
            print(step)
        break

    for new in moves(state):
        if new not in visited:
            visited.add(new)
            queue.append((new, path + [state]))