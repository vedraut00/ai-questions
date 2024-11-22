import copy

# Helper function: Calculate the Manhattan distance
def manhattan_distance(state, goal):
    distance = 0
    for i in range(1, 9):  # Tiles 1 to 8
        x1, y1 = [(x, y) for x, row in enumerate(state) for y, val in enumerate(row) if val == i][0]
        x2, y2 = [(x, y) for x, row in enumerate(goal) for y, val in enumerate(row) if val == i][0]
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Helper function: Find the blank (zero) position
def find_blank(state):
    for i, row in enumerate(state):
        for j, val in enumerate(row):
            if val == 0:
                return (i, j)

# Helper function: Generate neighbors by moving the blank tile
def generate_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:  # Ensure moves are within bounds
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    
    return neighbors

# Hill Climbing Algorithm
def hill_climbing(initial_state, goal_state):
    current_state = initial_state
    current_heuristic = manhattan_distance(current_state, goal_state)
    steps = 0
    
    while True:
        neighbors = generate_neighbors(current_state)
        next_state = None
        next_heuristic = float('inf')
        
        # Evaluate all neighbors and choose the one with the lowest heuristic
        for neighbor in neighbors:
            heuristic = manhattan_distance(neighbor, goal_state)
            if heuristic < next_heuristic:
                next_state = neighbor
                next_heuristic = heuristic

        # Check if we have reached the goal
        if next_heuristic == 0:
            print("Goal reached!")
            return next_state, steps

        # If no better neighbor is found, stop (local maxima or plateau)
        if next_heuristic >= current_heuristic:
            print("Stuck at local maxima or plateau!")
            return current_state, steps

        # Move to the better neighbor
        current_state = next_state
        current_heuristic = next_heuristic
        steps += 1
        print(f"Step {steps}: Heuristic = {current_heuristic}")
        print(f"State: {current_state}")

# Example Input and Execution
initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

result, steps = hill_climbing(initial_state, goal_state)
print(f"Final State: {result} in {steps} steps.")

