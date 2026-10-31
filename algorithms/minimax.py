def check_winner(board):
    """
    Check whether X or O has won the game.
    Return X, O, or None.
    """

    winning_combinations = [
        (0, 1, 2),  # Top row
        (3, 4, 5),  # Middle row
        (6, 7, 8),  # Bottom row
        (0, 3, 6),  # Left column
        (1, 4, 7),  # Middle column
        (2, 5, 8),  # Right column
        (0, 4, 8),  # Main diagonal
        (2, 4, 6)   # Other diagonal
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]

    return None


def is_draw(board):
    """Check whether the board is full and nobody has won."""

    return check_winner(board) is None and "" not in board

def minimax(board, is_maximizing, stats=None, depth=0):
    """
    Minimax algorithm with depth-aware scoring.

    AI = O
    Human = X

    Faster AI wins receive higher scores.
    Delayed AI losses receive higher scores.
    """

    # Count the current state
    if stats is not None:
        stats["states_explored"] += 1

    # Check the winner
    winner = check_winner(board)

    # AI wins: prefer winning quickly
    if winner == "O":
        return 10 - depth

    # Human wins: prefer delaying the loss
    if winner == "X":
        return depth - 10

    # Draw
    if "" not in board:
        return 0

    # AI's turn: maximize the score
    if is_maximizing:
        best_score = float("-inf")

        for i in range(9):
            if board[i] == "":
                board[i] = "O"

                score = minimax(
                    board,
                    False,
                    stats,
                    depth + 1
                )

                # Undo the move
                board[i] = ""

                best_score = max(best_score, score)

        return best_score

    # Human's turn: minimize the score
    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == "":
                board[i] = "X"

                score = minimax(
                    board,
                    True,
                    stats,
                    depth + 1
                )

                # Undo the move
                board[i] = ""

                best_score = min(best_score, score)

        return best_score

def best_move(board):
    """Find the best move for the AI."""

    best_score = float("-inf")
    move = None

    for i in range(9):
        if board[i] == "":
            board[i] = "O"

            score = minimax(board, False)

            board[i] = ""

            if score > best_score:
                best_score = score
                move = i

    return move
def best_move_minimax_with_stats(board):

    stats = {
        "states_explored": 0
    }

    best_score = float("-inf")
    move = None

    for i in range(9):

        if board[i] == "":

            board[i] = "O"

            score = minimax(board, False, stats)

            board[i] = ""

            if score > best_score:
                best_score = score
                move = i

    return move, stats
