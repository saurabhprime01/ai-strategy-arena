from algorithms.greedy import greedy

maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

explored, path, execution_time = greedy(
    maze,
    start,
    goal
)

print("Explored cells:", explored)
print("Final path:", path)
print("Explored cell count:", len(explored))
print("Path length:", len(path) - 1 if path else 0)
print(f"Execution time: {execution_time * 1000:.3f} ms")