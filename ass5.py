from collections import deque

def moves(state):
    result = []
    stacks = [list(s) for s in state]

    for i in range(len(stacks)):
        if not stacks[i]:
            continue

        block = stacks[i][-1]

        for j in range(len(stacks)):
            if i != j:
                new = [s[:] for s in stacks]
                new[i].pop()
                new[j].append(block)
                result.append(tuple(tuple(s) for s in new if s))

        new = [s[:] for s in stacks]
        new[i].pop()
        new.append([block])
        result.append(tuple(tuple(s) for s in new if s))

    return result

start = (('C', 'B', 'A'),)
goal = (('A', 'B', 'C'),)

queue = deque([(start, [])])
visited = {start}

while queue:
    state, path = queue.popleft()

    if state == goal:
        for step in path + [state]:
            print(step)
        break

    for new in moves(state):
        if new not in visited:
            visited.add(new)
            queue.append((new, path + [state]))
else:
    print("No solution")