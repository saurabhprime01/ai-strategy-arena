import heapq
import time


def heuristic(position, goal):
    """Calculate Manhattan distance between two cells."""

    row1, col1 = position
    row2, col2 = goal

    return abs(row1 - row2) + abs(col1 - col2)


def greedy(maze, start, goal):
    """Find a path using Greedy Best-First Search."""

    start_time = time.perf_counter()

    # Priority queue stores (heuristic, cell).
    priority_queue = []

    heapq.heappush(
        priority_queue,
        (heuristic(start, goal), start)
    )

    # Track each cell's parent.
    parent = {start: None}

    explored = []

    rows = len(maze)
    cols = len(maze[0])

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    while priority_queue:

        # Select the cell with the smallest heuristic.
        _, current = heapq.heappop(priority_queue)

        explored.append(current)

        if current == goal:
            break

        row, col = current

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            # Check maze boundaries.
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue

            # Ignore walls.
            if maze[nr][nc] == 1:
                continue

            next_cell = (nr, nc)

            # Avoid revisiting cells.
            if next_cell not in parent:

                parent[next_cell] = current

                priority = heuristic(next_cell, goal)

                heapq.heappush(
                    priority_queue,
                    (priority, next_cell)
                )

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