from collections import deque
import time


def bfs(maze, start, goal):
    """
    Find the shortest path through a maze using BFS.

    0 = Walkable cell
    1 = Wall
    """

    start_time = time.perf_counter()

    # Queue stores cells waiting to be explored.
    queue = deque([start])

    # Track each cell's predecessor.
    parent = {start: None}

    # Store cells in the order they are explored.
    explored = []

    rows = len(maze)
    cols = len(maze[0])

    # Up, down, left, right.
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while queue:
        current = queue.popleft()
        explored.append(current)

        # Stop when we reach the destination.
        if current == goal:
            break

        row, col = current

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            # Check whether the new cell is inside the maze.
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue

            # Skip walls.
            if maze[nr][nc] == 1:
                continue

            next_cell = (nr, nc)

            # Avoid revisiting cells.
            if next_cell not in parent:
                parent[next_cell] = current
                queue.append(next_cell)

    # Reconstruct the shortest path.
    path = []

    if goal in parent:
        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

    execution_time = time.perf_counter() - start_time

    return explored, path, execution_time