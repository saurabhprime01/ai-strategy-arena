from algorithms.minimax import best_move
from algorithms.alpha_beta import best_move_alpha_beta

# Example board
board = [
    "X", "X", "",
    "O", "", "",
    "", "", "O"
]

# Test Minimax
minimax_board = board.copy()

minimax_move = best_move(minimax_board)

print("Minimax best move:", minimax_move)

# Test Alpha-Beta Pruning
alpha_beta_board = board.copy()

alpha_beta_move, stats = best_move_alpha_beta(
    alpha_beta_board
)

print("Alpha-Beta best move:", alpha_beta_move)

print(
    "Alpha-Beta states explored:",
    stats["states_explored"]
)

# Both algorithms should block the human's winning move.
assert minimax_move == 2
assert alpha_beta_move == 2

print("Both algorithms passed the test!")
