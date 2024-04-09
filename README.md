# Project Overview

This project encompasses several fundamental modules:

- **astar.py:** This module implements the A* algorithm for pathfinding.
- **lidar.py:** Python script for retrieving lidar data.
- **obstacle_detection.py:** Simple code for detecting obstacles.
- **basic.py:** Module for basic movement functionalities.
- **location.py:** Module for robot localization in 3D space.

## Module Descriptions

### astar.py

The `astar.py` file contains the implementation of the A* algorithm, which is commonly used for path planning in various applications.

#### Interface:

- `find_path(start, goal, grid)`: Finds the optimal path from start to goal on the given grid.

### lidar.py

The `lidar.py` file serves as a Python script to acquire lidar data. It is tailored to work with the LDS-01 lidar sensor to retrieve real-time distance measurements.

#### Interface:

- `get_lidar_data()`: Retrieves lidar data from the sensor.

### obstacle_detection.py

The `obstacle_detection.py` module consists of straightforward code for detecting obstacles. It relies on lidar sensor data but does not incorporate advanced path planning or obstacle avoidance features.

#### Interface:

- `detect_obstacles(data)`: Detects obstacles in lidar data and returns their positions.

### basic.py

The `basic.py` module provides basic movement functionalities for a robot.

#### Interface:

- `move_forward(distance)`: Moves the robot forward by the specified distance.
- `turn(angle)`: Turns the robot by the specified angle.

### location.py

The `location.py` module implements robot localization in 3D space using linear acceleration and angular velocity data.

#### Interface:

- `update_position(linear_acceleration, angular_velocity, dt)`: Updates the position of the robot based on linear acceleration and angular velocity data.

## Usage

Each module is designed to be used independently. Refer to the comments within each file for detailed usage instructions.
