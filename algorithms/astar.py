import heapq
import time


def heuristic(position, goal):
    """Calculate Manhattan distance."""

    row1, col1 = position
    row2, col2 = goal

    return abs(row1 - row2) + abs(col1 - col2)


def astar(maze, start, goal):
    """Find the shortest path using A* Search."""

    start_time = time.perf_counter()

    # Priority queue stores (f_score, cell).
    priority_queue = []

    # Initially, g(start) = 0.
    heapq.heappush(
        priority_queue,
        (heuristic(start, goal), start)
    )

    # Actual cost from start to each cell.
    g_score = {start: 0}

    # Track each cell's parent.
    parent = {start: None}

    explored = []
    closed = set()

    rows = len(maze)
    cols = len(maze[0])

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    while priority_queue:

        _, current = heapq.heappop(priority_queue)

        # Ignore outdated queue entries.
        if current in closed:
            continue

        closed.add(current)
        explored.append(current)

        # Stop when the goal is reached.
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

            neighbor = (nr, nc)

            # Every movement costs 1.
            tentative_g = g_score[current] + 1

            # Update if we found a better route.
            if tentative_g < g_score.get(neighbor, float("inf")):

                g_score[neighbor] = tentative_g
                parent[neighbor] = current

                f_score = (
                    tentative_g
                    + heuristic(neighbor, goal)
                )

                heapq.heappush(
                    priority_queue,
                    (f_score, neighbor)
                )

                # Allow a better route to reopen a cell.
                closed.discard(neighbor)

    # Reconstruct the final path.
    path = []

    if goal in parent:

        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

    execution_time = time.perf_counter() - start_time

    return explored, path, execution_time