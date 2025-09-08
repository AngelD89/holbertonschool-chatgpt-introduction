#!/usr/bin/python3
def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 5)


def check_winner(board):
    """Return 'X' or 'O' if someone has won, else None."""
    lines = []

    # Rows and columns
    lines.extend(board)
    cols = [[board[r][c] for r in range(3)] for c in range(3)]
    lines.extend(cols)

    # Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] != " " and all(cell == line[0] for cell in line):
            return line[0]
    return None


def board_full(board):
    return all(cell != " " for row in board for cell in row)


def read_move(player):
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Please enter numbers (0, 1, or 2).")
            continue
        if row not in (0, 1, 2) or col not in (0, 1, 2):
            print("Row/column must be 0, 1, or 2.")
            continue
        return row, col


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        row, col = read_move(player)
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
