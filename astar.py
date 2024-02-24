import heapq
import numpy as np

class Node:
    def __init__(self, position, cost, parent=None):
        self.position = position
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(current, goal):
    # Manhattan distance
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def astar(grid, start, goal):
    open_set = []
    closed_set = set()

    start_node = Node(start, 0)
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.position)

        for neighbor in get_neighbors(grid, current_node.position):
            if neighbor in closed_set:
                continue

            cost = current_node.cost + 1
            neighbor_node = Node(neighbor, cost, current_node)

            if neighbor_node not in open_set:
                heapq.heappush(open_set, neighbor_node)

    return None

# def get_neighbors(grid, position):
#     neighbors = []
#     for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         new_position = (position[0] + move[0], position[1] + move[1])
#         if 0 <= new_position[0] < len(grid) and 0 <= new_position[1] < len(grid[0]) and grid[new_position[0]][new_position[1]] != 1:
#             neighbors.append(new_position)
#     return neighbors

def obstacle_detection_test():
    return np.random.uniform(0.0, 1.0, (5, 5))

def get_neighbors(grid, position):
    # lidar_data = obstacle_detection_test()  
    neighbors = []
    for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_position = (position[0] + move[0], position[1] + move[1])
        if (
            0 <= new_position[0] < len(grid)
            and 0 <= new_position[1] < len(grid[0])
            and grid[int(new_position[0])][int(new_position[1])] != 1
            # and lidar_data[int(new_position[0])][int(new_position[1])] > 0.5
        ):
            neighbors.append(new_position)
    return neighbors

#test
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)

if path:
    print("path found", path)
else:
    print("no path found")

# print(obstacle_detection_test())
