from algorithms.bfs import bfs

maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

explored, path = bfs(maze, start, goal)

print("Explored cells:", explored)
print("Final path:", path)
print("Number of explored cells:", len(explored))
print("Path length:", len(path) - 1 if path else 0)