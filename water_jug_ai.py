# Program for water jug problem using uninformed search 
initial_state = [0, 0]
target_state = [2, 0]
jug1_capacity = 4
jug2_capacity = 3

def water(state):
    jug1 = state[0]
    jug2 = state[1]
    return jug1 == target_state[0] and jug2 == target_state[1]

def successors(state):
    jug1 = state[0]
    jug2 = state[1]
    return [[jug1_capacity, jug2], [jug1, jug2_capacity], [0, jug2], [jug1, 0], [jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)], [jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)]]

def breadth_first_search(initial_state):
    frontier = [[initial_state]]
    while frontier:
        path = frontier.pop(0)
        state = path[-1]
        if water(state):
            return path
        for successor in successors(state):
            if successor not in path:
                frontier.append(path + [successor]) 
            
print(breadth_first_search(initial_state))




