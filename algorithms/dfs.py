import time


def dfs(maze, start, goal):
    """Find a path through a maze using Depth-First Search."""

    start_time = time.perf_counter()

    # Stack stores cells waiting to be explored.
    stack = [start]

    # Track each cell's parent.
    parent = {start: None}

    # Store the exploration order.
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

    while stack:
        current = stack.pop()
        explored.append(current)

        if current == goal:
            break

        row, col = current

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            # Ignore positions outside the maze.
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue

            # Ignore walls.
            if maze[nr][nc] == 1:
                continue

            next_cell = (nr, nc)

            # Avoid visiting a cell more than once.
            if next_cell not in parent:
                parent[next_cell] = current
                stack.append(next_cell)

    # Reconstruct the path.
    path = []

    if goal in parent:
        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

    execution_time = time.perf_counter() - start_time

    return explored, path, execution_time