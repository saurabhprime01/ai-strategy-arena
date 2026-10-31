from algorithms.minimax import check_winner
def alpha_beta(
    board,
    is_maximizing,
    alpha,
    beta,
    stats,
    depth=0
):
    """
    Minimax with Alpha-Beta Pruning and depth-aware scoring.

    AI = O
    Human = X
    """

    # Count the current state
    stats["states_explored"] += 1

    # Check the winner
    winner = check_winner(board)

    # AI wins quickly
    if winner == "O":
        return 10 - depth

    # Delay an unavoidable loss
    if winner == "X":
        return depth - 10

    # Draw
    if "" not in board:
        return 0

    # AI maximizes the score
    if is_maximizing:
        best_score = float("-inf")

        for i in range(9):
            if board[i] == "":
                board[i] = "O"

                score = alpha_beta(
                    board,
                    False,
                    alpha,
                    beta,
                    stats,
                    depth + 1
                )

                # Undo the move
                board[i] = ""

                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                # Prune unnecessary branches
                if beta <= alpha:
                    break

        return best_score

    # Human minimizes the score
    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == "":
                board[i] = "X"

                score = alpha_beta(
                    board,
                    True,
                    alpha,
                    beta,
                    stats,
                    depth + 1
                )

                # Undo the move
                board[i] = ""

                best_score = min(best_score, score)
                beta = min(beta, best_score)

                # Prune unnecessary branches
                if beta <= alpha:
                    break

        return best_score


def best_move_alpha_beta(board):
    """
    Find the best AI move using Alpha-Beta Pruning.
    Returns the move index and search statistics.
    """

    best_score = float("-inf")
    move = None

    stats = {"states_explored": 0}

    alpha = float("-inf")
    beta = float("inf")

    for i in range(9):

        if board[i] == "":

            # Try the AI move
            board[i] = "O"

            score = alpha_beta(
                board,
                False,
                alpha,
                beta,
                stats
            )

            # Undo the move
            board[i] = ""

            if score > best_score:
                best_score = score
                move = i

            alpha = max(alpha, best_score)

    return move, stats
