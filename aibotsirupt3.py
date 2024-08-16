import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors

# Define the grid size
grid_size = 5

# Create the grid with some dirt
np.random.seed(0)
grid = np.random.choice([0, 1], size=(grid_size, grid_size), p=[0.7, 0.3])

# Initial position of the vacuum cleaner
vacuum_pos = [0, 0]

# Function to visualize the grid
def plot_grid(grid, vacuum_pos, ax):
    ax.clear()
    cmap = colors.ListedColormap(['white', 'black'])
    ax.imshow(grid, cmap=cmap, vmin=0, vmax=1)
    ax.scatter(vacuum_pos[1], vacuum_pos[0], c='red', s=200, marker='s')
    ax.set_xticks(range(grid_size))
    ax.set_yticks(range(grid_size))
    ax.grid(True)

# Define actions
ACTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
    "CLEAN": (0, 0)
}

# Function to perform an action
def perform_action(grid, vacuum_pos, action):
    if action == "CLEAN":
        if grid[vacuum_pos[0], vacuum_pos[1]] == 1:  # Check if the current position is dirty
            grid[vacuum_pos[0], vacuum_pos[1]] = 0  # Clean the dirt
    else:  # update position
        new_pos = [vacuum_pos[0] + ACTIONS[action][0], vacuum_pos[1] + ACTIONS[action][1]]
        if (0 <= new_pos[0] < grid_size) and (0 <= new_pos[1] < grid_size):
            vacuum_pos[0], vacuum_pos[1] = new_pos
    return grid, vacuum_pos

# Function to find the nearest dirty cell
def find_nearest_dirty(grid, vacuum_pos):
    dirty_cells = np.argwhere(grid == 1)
    if len(dirty_cells) == 0:
        return None
    distances = np.linalg.norm(dirty_cells - vacuum_pos, axis=1)
    nearest_dirty = dirty_cells[np.argmin(distances)]
    return nearest_dirty

# Function to plan a path to the nearest dirty cell
def plan_path(vacuum_pos, nearest_dirty):
    path = []
    while not np.array_equal(vacuum_pos, nearest_dirty):
        if vacuum_pos[0] < nearest_dirty[0]:
            path.append("DOWN")
            vacuum_pos[0] += 1
        elif vacuum_pos[0] > nearest_dirty[0]:
            path.append("UP")
            vacuum_pos[0] -= 1
        if vacuum_pos[1] < nearest_dirty[1]:
            path.append("RIGHT")
            vacuum_pos[1] += 1
        elif vacuum_pos[1] > nearest_dirty[1]:
            path.append("LEFT")
            vacuum_pos[1] -= 1
    path.append("CLEAN")
    return path

# Initialize the plot
fig, ax = plt.subplots()

def update_plot(frame, grid, vacuum_pos, ax):
    nearest_dirty = find_nearest_dirty(grid, vacuum_pos)
    if nearest_dirty is not None:
        path = plan_path(vacuum_pos.copy(), nearest_dirty)
        for action in path:
            grid, vacuum_pos = perform_action(grid, vacuum_pos, action)
            plot_grid(grid, vacuum_pos, ax)
            plt.pause(0.1)  # pause for 0.1 seconds to see the animation
    else:
        plot_grid(grid, vacuum_pos, ax)
    return grid, vacuum_pos

# Create the animation
ani = animation.FuncAnimation(
    fig, update_plot, frames=None, fargs=(grid, vacuum_pos, ax), interval=1000, repeat=False
)

plt.show()  