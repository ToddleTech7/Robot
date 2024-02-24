import numpy as np
import cv2
import matplotlib.pyplot as plt

# initial location
pose_x = 0
pose_y = 0
pose_theta = 0

# lidar data


def obstacle_detection_simulator(grid, robot_position, max_range=5.0):
    lidar_data = np.zeros_like(grid, dtype=float)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            distance = np.linalg.norm(np.array([i, j]) - np.array(robot_position))
            if distance <= max_range:
                lidar_data[i][j] = 1.0

    return lidar_data

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
robot_position = (2.0, 2.0)

lidar_data = obstacle_detection_simulator(grid, robot_position)
print(lidar_data)
