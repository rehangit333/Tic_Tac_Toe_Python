# Tic Tac Toe Game

# Function to display the board
def display_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---+---+---")

# Function to check for a win or a draw
def check_win(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "-":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return True
    return False

def check_draw(board):
    return all(cell != "-" for row in board for cell in row)

# Save the game state to a file
def save_game(board, current_player):
    with open("game_state.txt", "w") as file:
        for row in board:
            file.write(",".join(row) + "\n")
        file.write(f"Player Turn: {current_player}\n")
    print("Game state saved!")

# Load the game state from a file
def load_game():
    try:
        with open("game_state.txt", "r") as file:
            lines = file.readlines()
            board = [line.strip().split(",") for line in lines[:-1]]
            current_player = lines[-1].split(":")[1].strip()
            return board, current_player
    except FileNotFoundError:
        print("No saved game found. Starting a new game.")
        return [["-", "-", "-"] for _ in range(3)], "X"
    except IndexError:
        print("Corrupted game state. Starting a new game.")
        return [["-", "-", "-"] for _ in range(3)], "X"

# Reset the game state to the initial state
def reset_game_state():
    with open("game_state.txt", "w") as file:
        file.write("")

# Main game loop
def main():
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X\nPlayer 2: O")

    board, current_player = load_game()

    while True:
        display_board(board)
        print(f"Player {current_player}, enter your move (1-9): ", end="")
        try:
            move = int(input()) - 1
            row, col = divmod(move, 3)
            if board[row][col] == "-":
                board[row][col] = current_player
                if check_win(board):
                    display_board(board)
                    print(f"Player {current_player} wins!")
                    reset_game_state()
                    print("Game has been reset to the initial state.")
                    break
                elif check_draw(board):
                    display_board(board)
                    print("It's a draw!")
                    reset_game_state()
                    print("Game has been reset to the initial state.")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Enter a number between 1 and 9.")

        # Offer to save the game after every move
        print("Do you want to save the game? (yes/no): ", end="")
        if input().strip().lower() == "yes":
            save_game(board, current_player)
            break

if __name__ == "__main__":
    main()
