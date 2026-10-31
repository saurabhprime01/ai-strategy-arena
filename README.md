# 🧠 AI Strategy Arena

**An Interactive Platform for Exploring Artificial Intelligence Algorithms**

AI Strategy Arena is an interactive application built with Python and Streamlit that demonstrates how different Artificial Intelligence algorithms solve problems and make decisions.

The platform allows users to explore search algorithms, play against an AI opponent, and compare algorithm performance through interactive visualizations.

## 🚀 Features

### 1. Maze Intelligence

Explore different pathfinding algorithms:

* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* Greedy Best-First Search
* A* Search

### 2. AI Game Arena

Play Tic-Tac-Toe against an AI opponent powered by:

* Minimax Algorithm
* Alpha-Beta Pruning

The AI attempts to make the optimal move using game-tree search.

### 3. Performance Lab

Explore and compare algorithm performance using metrics such as execution time and explored states.

### 4. Sudoku Intelligence

Coming Soon!

## 🛠️ Technology Stack

* **Language:** Python
* **Frontend:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib
* **Testing:** Pytest
* **Version Control:** Git and GitHub

## 📂 Project Structure

```text
AI_Strategy_Arena/
│
├── algorithms/
│   ├── alpha_beta.py
│   ├── astar.py
│   ├── bfs.py
│   ├── dfs.py
│   ├── greedy.py
│   └── minimax.py
│
├── tests/
│   ├── test_alpha_beta.py
│   ├── test_astar.py
│   ├── test_bfs.py
│   ├── test_dfs.py
│   ├── test_greedy.py
│   ├── test_minmax.py
│   └── test_tictactoe.py
│
├── utils/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/saurabhprime01/ai-strategy-arena.git
```

### 2. Navigate to the project directory

```bash
cd ai-strategy-arena
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🧪 Running Tests

Run the test suite using:

```bash
python -m pytest tests/ -v
```

## 🎯 Project Goals

* Understand the practical implementation of AI algorithms.
* Visualize how search algorithms explore different paths.
* Understand decision-making through game-tree search.
* Compare algorithm performance.
* Build an interactive learning experience.

## 🔮 Future Improvements

* Implement a complete Sudoku solver using backtracking.
* Add more AI algorithms.
* Improve interactive visualizations.
* Add more games and problem-solving challenges.

## 👨‍💻 Contributors

Developed as a collaborative AI project.

## 📄 License

This project is currently available for educational and learning purposes. A formal open-source license may be added later.
