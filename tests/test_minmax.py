from algorithms.minimax import best_move, check_winner

# Empty Tic-Tac-Toe board
board = [
    "X", "X", "",
    "O", "", "",
    "", "", "O"
]

move = best_move(board)

print("Best move index:", move)

# Apply the AI's move
if move is not None:
    board[move] = "O"

print("Updated board:")

for i in range(0, 9, 3):
    print(board[i:i + 3])

print("Winner:", check_winner(board))
