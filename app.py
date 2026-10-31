import time
import random

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.greedy import greedy
from algorithms.astar import astar
from algorithms.minimax import best_move_minimax_with_stats
from algorithms.alpha_beta import best_move_alpha_beta


# ---------------------------------------
# 1. PAGE CONFIGURATION
# ---------------------------------------

st.set_page_config(
    page_title="AI Strategy Arena",
    page_icon="🧠",
    layout="wide"
)


# ---------------------------------------
# 2. MAZE GENERATION
# ---------------------------------------

def generate_maze(size, wall_density, seed):
    """
    Generate a random maze.

    0 = Empty cell
    1 = Wall
    """

    rng = random.Random(seed)

    maze = np.zeros((size, size), dtype=int)

    for row in range(size):
        for col in range(size):
            if rng.random() < wall_density:
                maze[row][col] = 1

    # Keep the top row and rightmost column open.
    # This guarantees a route from start to goal.
    maze[0, :] = 0
    maze[:, size - 1] = 0

    return maze.tolist()


# ---------------------------------------
# 3. DRAW THE MAZE
# ---------------------------------------

def draw_maze(maze, explored=None, path=None):
    """
    Draw the maze and its explored cells and final path.
    """

    if explored is None:
        explored = set()

    if path is None:
        path = set()

    size = len(maze)

    # Make a separate grid for visualization.
    display_grid = np.array(maze, dtype=int)

    # Color explored cells blue.
    for row, col in explored:
        if (row, col) not in [(0, 0), (size - 1, size - 1)]:
            display_grid[row, col] = 2

    # Color final path green.
    for row, col in path:
        if (row, col) not in [(0, 0), (size - 1, size - 1)]:
            display_grid[row, col] = 3

    # Mark start and goal.
    display_grid[0, 0] = 4
    display_grid[size - 1, size - 1] = 5

    colors = [
        "#FFFFFF",  # Empty
        "#1F2937",  # Wall
        "#93C5FD",  # Explored
        "#22C55E",  # Final path
        "#FACC15",  # Start
        "#EF4444"   # Goal
    ]

    cmap = ListedColormap(colors)

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.imshow(
        display_grid,
        cmap=cmap,
        vmin=0,
        vmax=5
    )

    # Draw grid lines.
    ax.set_xticks(np.arange(-0.5, size, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, size, 1), minor=True)

    ax.grid(
        which="minor",
        color="#D1D5DB",
        linestyle="-",
        linewidth=0.5
    )

    ax.tick_params(
        which="both",
        bottom=False,
        left=False,
        labelbottom=False,
        labelleft=False
    )

    ax.set_title("AI Maze Visualization")

    return fig


# ---------------------------------------
# 4. APPLICATION HEADER
# ---------------------------------------

st.title("🧠 AI Strategy Arena")

st.markdown(
    "### An Interactive Platform for Intelligent Problem-Solving"
)

st.write(
    "Explore how artificial intelligence algorithms "
    "search through mazes and discover paths."
)

st.divider()


# ---------------------------------------
# 5. SIDEBAR NAVIGATION
# ---------------------------------------

section = st.sidebar.radio(
    "Choose an Arena",
    [
        "Home",
        "Maze Intelligence",
        "AI Game Arena",
        "Performance Lab",
        "Sudoku Intelligence"
    ]
)


# ---------------------------------------
# 6. HOME PAGE
# ---------------------------------------

if section == "Home":

    st.header("Welcome to AI Strategy Arena")

    col1, col2, col3 = st.columns(3)

    col1.metric("Search Algorithms", "4")
    col2.metric("AI Game Engines", "1")
    col3.metric("Puzzle Solvers", "1")

    st.info(
        "Select Maze Intelligence from the sidebar "
        "to explore your first AI algorithm."
    )


# ---------------------------------------
# 7. MAZE INTELLIGENCE
# ---------------------------------------

elif section == "Maze Intelligence":

    st.header("🧩 Maze Intelligence")

    st.write(
        "Watch Breadth-First Search explore a maze "
        "and find the shortest path."
    )

    # User controls.
    col1, col2, col3 = st.columns(3)

    with col1:
        size = st.slider(
            "Maze size",
            min_value=10,
            max_value=25,
            value=15
        )

    with col2:
        wall_density = st.slider(
            "Wall density",
            min_value=0.10,
            max_value=0.40,
            value=0.25,
            step=0.05
        )

    with col3:
        animation_speed = st.slider(
            "Animation delay (seconds)",
            min_value=0.0,
            max_value=0.10,
            value=0.02,
            step=0.01
        )

    # Keep the same maze until the user generates a new one.
    if "maze_seed" not in st.session_state:
        st.session_state.maze_seed = 42

    if st.button("🔄 Generate New Maze"):
        st.session_state.maze_seed += 1

    maze = generate_maze(
        size,
        wall_density,
        st.session_state.maze_seed
    )

    start = (0, 0)
    goal = (size - 1, size - 1)

    st.markdown(
        "**Legend:** 🟨 Start | 🟥 Goal | "
        "⬛ Wall | 🟦 Explored | 🟩 Final path"
    )

    algorithm_choice = st.selectbox(
        "Choose a Search Algorithm",
        ["BFS", "DFS", "Greedy Best-First Search", "A* Search"]
    )
    # Display the initial maze.
    maze_placeholder = st.empty()

    fig = draw_maze(maze)
    maze_placeholder.pyplot(fig)
    plt.close(fig)

    # Run the algorithm.
    if st.button("▶️ Run Search", type="primary"):

        if algorithm_choice == "BFS":
            explored, path, execution_time = bfs(
                maze,
                start,
                goal
            )

        elif algorithm_choice == "DFS":
            explored, path, execution_time = dfs(
                maze,
                start,
                goal
            )
        elif algorithm_choice == "Greedy Best-First Search":
            explored, path, execution_time = greedy(
                maze, start, goal

            )
        else:
            explored, path, execution_time = astar(
                maze, start, goal
                
            )

        progress = st.progress(0)
        status = st.empty()

        # Display the exploration animation.
        total = len(explored)

        batch_size = max(1, total // 50)

        for i in range(0, total, batch_size):

            explored_so_far = set(
                explored[:i + batch_size]
            )

            fig = draw_maze(
                maze,
                explored=explored_so_far
            )

            maze_placeholder.pyplot(fig)
            plt.close(fig)

            progress.progress(
                min(1.0, (i + batch_size) / total)
            )

            status.write(
                f"Exploring cells: {min(i + batch_size, total)} "
                f"/ {total}"
            )

            if animation_speed > 0:
                time.sleep(animation_speed)

        # Display the final path.
        fig = draw_maze(
            maze,
            explored=set(explored),
            path=set(path)
        )

        maze_placeholder.pyplot(fig)
        plt.close(fig)

        status.success("Search completed!")

        # Performance metrics.
        st.divider()
        st.subheader("📊 BFS Performance")

        metric1, metric2, metric3 = st.columns(3)

        metric1.metric(
            "Explored Cells",
            len(explored)
        )

        metric2.metric(
            "Path Length",
            len(path) - 1 if path else 0
        )

        metric3.metric(
            "Execution Time",
            f"{execution_time * 1000:.3f} ms"
        )

        if path:
            st.success(
                "BFS found the shortest path to the goal!"
            )
        else:
            st.error(
                "No path was found. Try generating another maze."
            )


# ---------------------------------------
# 8. OTHER MODULES
# ---------------------------------------

# elif section == "AI Game Arena":

#     st.header("🎮 AI Game Arena")

#     st.write(
#         "We will build a Tic-Tac-Toe AI using "
#         "Minimax and Alpha-Beta Pruning in a later step."
#     )

elif section == "AI Game Arena":

    from algorithms.minimax import best_move, check_winner

    st.header("🎮 AI Game Arena")
    st.write("Challenge an AI powered by the Minimax algorithm!")

    st.divider()

    # Initialize the game board
    if "ttt_board" not in st.session_state:
        st.session_state.ttt_board = [""] * 9

    if "ttt_game_over" not in st.session_state:
        st.session_state.ttt_game_over = False

    if "ttt_message" not in st.session_state:
        st.session_state.ttt_message = "Your turn! You are X."

    def reset_ttt():
        st.session_state.ttt_board = [""] * 9
        st.session_state.ttt_game_over = False
        st.session_state.ttt_message = "Your turn! You are X."

    # Restart button
    if st.button("🔄 New Game"):
        reset_ttt()

    board = st.session_state.ttt_board
    winner = check_winner(board)

    ai_strategy = st.selectbox(
    "Choose AI Strategy",
    [
        "Minimax",
        "Alpha-Beta Pruning"
    ]
)

    # Display the board
    for row in range(3):

        columns = st.columns(3)

        for col in range(3):

            index = row * 3 + col

            with columns[col]:

                label = board[index] if board[index] else " "

                if st.button(
                    label,
                    key=f"ttt_cell_{index}",
                    use_container_width=True,
                    disabled=(
                        board[index] != ""
                        or st.session_state.ttt_game_over
                    )
                ):

                    # Human makes a move
                    board[index] = "X"

                    winner = check_winner(board)

                    if winner == "X":
                        st.session_state.ttt_message = (
                            "🎉 Congratulations! You won!"
                        )
                        st.session_state.ttt_game_over = True

                    elif "" not in board:
                        st.session_state.ttt_message = (
                            "🤝 It's a draw!"
                        )
                        st.session_state.ttt_game_over = True

                    else:
                        # AI makes its move
                        # Select the AI algorithm based on the user's choice
                        
                        # ---------------------------------------
                        # AI DECISION AND PERFORMANCE STATISTICS
                        # ---------------------------------------

                        start_time = time.perf_counter()

                        if ai_strategy == "Minimax":

                            ai_move, stats = best_move_minimax_with_stats(board.copy())

                        else:

                            ai_move, stats = best_move_alpha_beta(board.copy())

                        execution_time = (time.perf_counter() - start_time) * 1000

                        # Store the latest AI performance statistics
                        st.session_state.ai_stats = {
                            "algorithm": ai_strategy,
                            "states_explored": stats["states_explored"],
                            "execution_time_ms": execution_time,
                            "selected_move": ai_move
                        }

                        # Apply the selected move to the actual game board
                        if ai_move is not None:
                            board[ai_move] = "O"

                        winner = check_winner(board)

                        if winner == "O":
                            st.session_state.ttt_message = (
                                "🤖 AI wins! Try again."
                            )
                            st.session_state.ttt_game_over = True

                        elif "" not in board:
                            st.session_state.ttt_message = (
                                "🤝 It's a draw!"
                            )
                            st.session_state.ttt_game_over = True

                        else:
                            st.session_state.ttt_message = (
                                "Your turn! You are X."
                            )

                    st.rerun()

    st.divider()

    # Game status
    st.subheader("Game Status")
    st.info(st.session_state.ttt_message)

    # ---------------------------------------
    # AI PERFORMANCE DASHBOARD
    # ---------------------------------------

    if "ai_stats" in st.session_state:

        stats = st.session_state.ai_stats

        st.divider()

        st.subheader("🧠 AI Decision Analytics")

        st.caption(
            f"Latest algorithm: {stats['algorithm']}"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "States Explored",
                stats["states_explored"]
            )

        with col2:
            st.metric(
                "Execution Time",
                f"{stats['execution_time_ms']:.4f} ms"
            )

        with col3:
            st.metric(
                "Selected Cell",
                stats["selected_move"]
                if stats["selected_move"] is not None
                else "None"
            )

    st.caption(
        "The AI uses Minimax to evaluate possible moves "
         "and select an optimal move."
    )
    # ---------------------------------------
    # AI ALGORITHM PERFORMANCE COMPARISON
    # ---------------------------------------

    st.divider()

    st.subheader("📊 Algorithm Performance Comparison")

    st.write(
        "Compare Minimax and Alpha-Beta Pruning "
        "on the same Tic-Tac-Toe board."
    )

    if st.button("🚀 Compare AI Algorithms"):

        # Copy the current board so the game is not modified.
        test_board = st.session_state.ttt_board.copy()

        # Measure Minimax
        start_time = time.perf_counter()

        minimax_move, minimax_stats = (
            best_move_minimax_with_stats(test_board.copy())
        )

        minimax_time = time.perf_counter() - start_time

        # Measure Alpha-Beta Pruning
        start_time = time.perf_counter()

        alpha_beta_move, alpha_beta_stats = (
            best_move_alpha_beta(test_board.copy())
        )

        alpha_beta_time = time.perf_counter() - start_time

        # Prepare comparison results
        results = pd.DataFrame({
            "Metric": [
                "Best Move (Cell Index)",
                "States Explored",
                "Execution Time (ms)"
            ],
            "Minimax": [
                minimax_move,
                minimax_stats["states_explored"],
                round(minimax_time * 1000, 4)
            ],
            "Alpha-Beta Pruning": [
                alpha_beta_move,
                alpha_beta_stats["states_explored"],
                round(alpha_beta_time * 1000, 4)
            ]
        })

        st.subheader("Comparison Results")

        st.dataframe(
            results,
            use_container_width=True,
            hide_index=True
        )

        # Calculate reduction in explored states
        minimax_states = minimax_stats["states_explored"]
        alpha_beta_states = alpha_beta_stats["states_explored"]

        if minimax_states > 0:

            reduction = (
                (minimax_states - alpha_beta_states)
                / minimax_states
            ) * 100

            st.metric(
                "Reduction in States Explored",
                f"{reduction:.2f}%"
            )

        # Compare the selected moves
        if minimax_move == alpha_beta_move:
            st.success(
                "Both algorithms selected the same move."
            )
        else:
            st.warning(
                "The algorithms selected different moves. "
                "Review their implementations."
            )

        # Display a bar chart
        chart_data = pd.DataFrame({
            "Algorithm": [
                "Minimax",
                "Alpha-Beta Pruning"
            ],
            "States Explored": [
                minimax_states,
                alpha_beta_states
            ]
        })

        st.subheader("States Explored by Each Algorithm")

        st.bar_chart(
            chart_data.set_index("Algorithm")
        )


elif section == "Performance Lab":

    st.header("📊 Algorithm Performance Lab")

    st.write(
        "Compare BFS, DFS, Greedy Best-First Search, and A* on the same maze."
    )

    st.divider()

    # -----------------------------------
    # 1. USER CONTROLS
    # -----------------------------------

    col1, col2 = st.columns(2)

    with col1:
        size = st.slider(
            "Maze size",
            min_value=10,
            max_value=25,
            value=15,
            key="performance_maze_size"
        )

    with col2:
        wall_density = st.slider(
            "Wall density",
            min_value=0.10,
            max_value=0.40,
            value=0.25,
            step=0.05,
            key="performance_wall_density"
        )

    # Keep the same maze during a comparison.
    if "performance_seed" not in st.session_state:
        st.session_state.performance_seed = 100

    if st.button("🔄 Generate New Comparison Maze"):
        st.session_state.performance_seed += 1

    maze = generate_maze(
        size,
        wall_density,
        st.session_state.performance_seed
    )

    start = (0, 0)
    goal = (size - 1, size - 1)

    # -----------------------------------
    # 2. DISPLAY THE MAZE
    # -----------------------------------

    st.subheader("Comparison Maze")

    fig = draw_maze(maze)
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    st.caption(
        "All four algorithms will run on this same maze."
    )

    # -----------------------------------
    # 3. RUN ALL ALGORITHMS
    # -----------------------------------

    if st.button(
        "🚀 Compare Algorithms",
        type="primary"
    ):

        algorithms = {
            "BFS": bfs,
            "DFS": dfs,
            "Greedy Best-First Search": greedy,
            "A* Search": astar
        }

        results = []

        for name, algorithm in algorithms.items():

            explored, path, execution_time = algorithm(
                maze,
                start,
                goal
            )

            results.append({
                "Algorithm": name,
                "Explored Cells": len(explored),
                "Path Length": (
                    len(path) - 1 if path else None
                ),
                "Execution Time (ms)": round(
                    execution_time * 1000,
                    4
                ),
                "Path Found": bool(path)
            })

        # Save results so they remain visible after reruns.
        st.session_state.performance_results = results

    # -----------------------------------
    # 4. DISPLAY COMPARISON RESULTS
    # -----------------------------------

    if "performance_results" in st.session_state:

        results = st.session_state.performance_results

        st.divider()
        st.subheader("📋 Comparison Results")

        st.dataframe(
            results,
            use_container_width=True,
            hide_index=True
        )

        # -----------------------------------
        # 5. METRICS
        # -----------------------------------

        successful_results = [
            result
            for result in results
            if result["Path Found"]
        ]

        if successful_results:

            best_path = min(
                successful_results,
                key=lambda result: result["Path Length"]
            )

            fastest = min(
                successful_results,
                key=lambda result: result["Execution Time (ms)"]
            )

            col1, col2 = st.columns(2)

            col1.metric(
                "Shortest Path Found",
                best_path["Path Length"],
                best_path["Algorithm"]
            )

            col2.metric(
                "Fastest in This Run",
                f'{fastest["Execution Time (ms)"]:.4f} ms',
                fastest["Algorithm"]
            )

        # -----------------------------------
        # 6. EXPLORED CELLS CHART
        # -----------------------------------

        st.divider()
        st.subheader("Cells Explored")

        names = [
            result["Algorithm"]
            for result in results
        ]

        explored_counts = [
            result["Explored Cells"]
            for result in results
        ]

        fig, ax = plt.subplots(figsize=(10, 4))

        ax.bar(names, explored_counts)

        ax.set_ylabel("Number of Cells")
        ax.set_xlabel("Algorithm")
        ax.set_title("Explored Cells by Algorithm")

        plt.xticks(rotation=15, ha="right")
        plt.tight_layout()

        st.pyplot(fig)
        plt.close(fig)

        # -----------------------------------
        # 7. EXECUTION TIME CHART
        # -----------------------------------

        st.subheader("Execution Time")

        times = [
            result["Execution Time (ms)"]
            for result in results
        ]

        fig, ax = plt.subplots(figsize=(10, 4))

        ax.bar(names, times)

        ax.set_ylabel("Execution Time (ms)")
        ax.set_xlabel("Algorithm")
        ax.set_title("Execution Time Comparison")

        plt.xticks(rotation=15, ha="right")
        plt.tight_layout()

        st.pyplot(fig)
        plt.close(fig)

        st.info(
            "Results depend on the maze, implementation, "
            "and computer. Very small timing differences "
            "may be caused by measurement noise."
        )


elif section == "Sudoku Intelligence":

    st.header("🔢 Sudoku Intelligence")

    st.write(
        "We will implement a Sudoku solver using "
        "backtracking in a later step."
    )