# 8 puzzle problem using heuristic search


# Program for 8 puzzle problem using heuristic search
import copy


def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def move(state, direction):
    new_state = copy.deepcopy(state)
    i, j = find_zero(state)
    if direction == 'up':
        new_state[i][j] = new_state[i - 1][j]
        new_state[i - 1][j] = 0
    elif direction == 'down':
        new_state[i][j] = new_state[i + 1][j]
        new_state[i + 1][j] = 0
    elif direction == 'left':
        new_state[i][j] = new_state[i][j - 1]
        new_state[i][j - 1] = 0
    elif direction == 'right':
        new_state[i][j] = new_state[i][j + 1]
        new_state[i][j + 1] = 0
    return new_state

def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != target_state[i][j]:
                h += 1
    return h

def successors(state):
    i, j = find_zero(state)
    successors = []
    if i > 0:
        successors.append(move(state, 'up'))
    if i < 2:
        successors.append(move(state, 'down'))
    if j > 0:
        successors.append(move(state, 'left'))
    if j < 2:
        successors.append(move(state, 'right'))
    return successors

def best_first_search(initial_state):
    frontier = [[heuristic(initial_state), initial_state]]
    while frontier:
        frontier.sort()
        path = frontier.pop(0)
        state = path[-1]
        if state == target_state:
            return path
        for successor in successors(state):
            if successor not in path:
                frontier.append([heuristic(successor), path + [successor]])
    return 'Failure'

initial_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
print(best_first_search(initial_state))


