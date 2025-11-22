# Tic Tac Toe Game in Python

# Function to print the board
def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

# Function to check if there is a winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for c in range(3):
        if all(board[r][c] == player for r in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if board is full
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Main function to play the game
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Player 1: X | Player 2: O")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn:")
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
        except ValueError:
            print("❌ Please enter valid integers between 0 and 2.")
            continue

        # Validate move
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == " ":
                board[row][col] = current_player
                print_board(board)

                # Check for win
                if check_winner(board, current_player):
                    print(f"🎉 Player {current_player} wins!")
                    break

                # Check for draw
                if is_draw(board):
                    print("🤝 It's a draw!")
                    break

                # Switch player
                current_player = "O" if current_player == "X" else "X"
            else:
                print("❌ That cell is already taken. Try again.")
        else:
            print("❌ Invalid position. Choose between 0 and 2.")

# Run the game
if __name__ == "__main__":
    play_tic_tac_toe()
