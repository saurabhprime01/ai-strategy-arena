from algorithms.minimax import (
    check_winner,
    is_draw,
    best_move_minimax_with_stats
)

from algorithms.alpha_beta import best_move_alpha_beta


# Test 1: Detect X as winner
def test_check_winner():

    board = [
        "X", "X", "X",
        "O", "O", "",
        "", "", ""
    ]

    assert check_winner(board) == "X"


# Test 2: Detect O as winner
def test_ai_winner():

    board = [
        "O", "O", "O",
        "X", "X", "",
        "", "", ""
    ]

    assert check_winner(board) == "O"


# Test 3: Minimax should find an immediate win
def test_minimax_winning_move():

    board = [
        "O", "O", "",
        "X", "X", "",
        "", "", ""
    ]

    move, stats = best_move_minimax_with_stats(board.copy())

    assert move == 2
    assert stats["states_explored"] > 0


# Test 4: Minimax should block human's winning move
def test_minimax_blocking_move():

    board = [
        "X", "X", "",
        "O", "", "",
        "", "", ""
    ]

    move, stats = best_move_minimax_with_stats(board.copy())

    assert move == 2


# Test 5: Alpha-Beta should find an immediate win
def test_alpha_beta_winning_move():

    board = [
        "O", "O", "",
        "X", "X", "",
        "", "", ""
    ]

    move, stats = best_move_alpha_beta(board.copy())

    assert move == 2
    assert stats["states_explored"] > 0


# Test 6: Alpha-Beta should block human
def test_alpha_beta_blocking_move():

    board = [
        "X", "X", "",
        "O", "", "",
        "", "", ""
    ]

    move, stats = best_move_alpha_beta(board.copy())

    assert move == 2


# Test 7: Both algorithms should preserve the board
def test_board_unchanged():

    board = [
        "O", "X", "",
        "", "X", "",
        "", "", "O"
    ]

    original_board = board.copy()

    best_move_minimax_with_stats(board)
    best_move_alpha_beta(board)

    assert board == original_board


# Test 8: Detect a draw
def test_draw():

    board = [
        "X", "O", "X",
        "X", "O", "O",
        "O", "X", "X"
    ]

    assert is_draw(board) is True