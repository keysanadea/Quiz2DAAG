# Dimensions
WIDTH = 480   # Width of game surface
HEIGHT = 480  # Height of game surface
ROWS = 12
SQUARE_SIZE = WIDTH // ROWS
GAP_SIZE = 4  # Gap between adjacent squares
# Colors
SURFACE_CLR = (255, 255, 255)
GRID_CLR = (60, 60, 60)
SNAKE_CLR = (150, 224, 246)
APPLE_CLR = (204,0,0)
HEAD_CLR = (98, 173, 196)
VIRTUAL_SNAKE_CLR = (255, 0, 0)
# Game Settings
FPS = 10000# Frames per second
INITIAL_SNAKE_LENGTH = 2
WAIT_SECONDS_AFTER_WIN = 5  # If snake wins the game, wait for this amount of seconds before restarting
MAX_MOVES_WITHOUT_EATING = ROWS * ROWS * ROWS * 0  # Snake will die after this amount of moves without eating apple
SNAKE_MAX_LENGTH = ROWS * ROWS - INITIAL_SNAKE_LENGTH  # Max number of apples snake can eat

# Variables used in BFS algorithm
GRID = [[i, j] for i in range(ROWS) for j in range(ROWS)]

# Helper functions
def get_neighbors(position):
    neighbors = [[position[0] + 1, position[1]],
                 [position[0] - 1, position[1]],
                 [position[0], position[1] + 1],
                 [position[0], position[1] - 1]]
    in_grid_neighbors = []
    for pos in neighbors:
        if pos in GRID:
            in_grid_neighbors.append(pos)
    return in_grid_neighbors

def distance(pos1, pos2):
    x1, x2 = pos1[0], pos2[0]
    y1, y2 = pos1[1], pos2[1]
    return abs(x2 - x1) + abs(y2 - y1)

# Each position is a tuple because python doesn't allow hashing lists
ADJACENCY_DICT = {tuple(pos): get_neighbors(pos) for pos in GRID}
