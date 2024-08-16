import pygame
import random
from collections import deque

# Initialize Pygame
pygame.init()

# Define constants
M, N = 20, 20  # Grid dimensions
CLEAN_COLOR = (255, 255, 255)  # White
DIRT_COLOR = (0, 0, 0)  # Black
VACUUM_COLOR = (255, 0, 0)  # Red

# Set up the display
screen = pygame.display.set_mode((M * 20, N * 20))

# Initialize the grid
grid = [[CLEAN_COLOR for _ in range(N)] for _ in range(M)]

# Randomly place dirt on the grid
for _ in range(M * N // 2):
    x, y = random.randint(0, M - 1), random.randint(0, N - 1)
    grid[x][y] = DIRT_COLOR

# Set the vacuum's starting position
vacuum_x, vacuum_y = 0, 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the grid
    for i in range(M):
        for j in range(N):
            color = grid[i][j]
            pygame.draw.rect(screen, color, (i * 20, j * 20, 20, 20))

    # Draw the vacuum
    pygame.draw.rect(screen, VACUUM_COLOR, (vacuum_x * 20, vacuum_y * 20, 20, 20))

    # Update the display
    pygame.display.flip()

    # Clean nearby dirt
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x, y = vacuum_x + dx, vacuum_y + dy
            if 0 <= x < M and 0 <= y < N and grid[x][y] == DIRT_COLOR:
                grid[x][y] = CLEAN_COLOR

    # Check if majority of nearby space is clear
    nearby_clear = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x, y = vacuum_x + dx, vacuum_y + dy
            if 0 <= x < M and 0 <= y < N and grid[x][y] == CLEAN_COLOR:
                nearby_clear += 1
    if nearby_clear >= 7:  # If majority of nearby space is clear
        # Use BFS to check if any dirt is remaining
        queue = deque([(vacuum_x, vacuum_y)])
        visited = {(vacuum_x, vacuum_y)}
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N and (nx, ny) not in visited:
                    if grid[nx][ny] == DIRT_COLOR:
                        running = True
                        break
                    queue.append((nx, ny))
                    visited.add((nx, ny))
            else:
                continue
            break
        else:
            running = False  # If no dirt is remaining, game ends

    # Move the vacuum
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]  # right, down, left, up, and diagonals
    for dx, dy in directions:
        x, y = vacuum_x + dx, vacuum_y + dy
        if 0 <= x < M and 0 <= y < N and grid[x][y] == DIRT_COLOR:
            vacuum_x, vacuum_y = x, y
            break
    else:
        # If no dirt is found nearby, move randomly
        dx, dy = random.choice(directions)
        x, y = vacuum_x + dx, vacuum_y + dy
        if 0 <= x < M and 0 <= y < N:
            vacuum_x, vacuum_y = x, y

    # Cap the frame rate
    pygame.time.delay(100)

# Quit Pygame
pygame.quit()
