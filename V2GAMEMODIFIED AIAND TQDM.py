import numpy as np
import time

# Step 1: Create the board
board = np.zeros((3, 3, 3))


# Step 2: Display the board
def display_board(board: object) -> object:
    """

    :rtype: object
    """
    print(board)


# Step 3: Check for a winner
def check_winner(board):
    # Check rows
    for i in range(3):
        for j in range(3):
            if board[i, j, 0] == board[i, j, 1] == board[i, j, 2] != 0:
                return True, board[i, j, 0]

    # Check columns
    for i in range(3):
        for j in range(3):
            if board[0, i, j] == board[1, i, j] == board[2, i, j] != 0:
                return True, board[0, i, j]

    # Check diagonals
    if board[0, 0, 0] == board[1, 1, 1] == board[2, 2, 2] != 0:
        return True, board[0, 0, 0]
    if board[0, 2, 0] == board[1, 1, 1] == board[2, 0, 2] != 0:
        return True, board[0, 2, 0]

    # Check for tie
    if np.all(board != 0):
        return True, None

    return False, None


# Step 4: Get player's move
def get_player_move():
    while True:
        try:
            move = tuple(map(int, input("Enter your move (x,y,z): ").split(',')))
            if board[move] == 0:
                return move
            else:
                print("Invalid move, try again")
        except ValueError:
            print("Invalid input, try again")


# Step 5: Get AI player's move using Minimax with alpha-beta pruning
def get_ai_move(board, level, player):
    if level == 1:
        # Easy level: choose a random move
        return tuple(np.random.randint(0, 3, 3))
    elif level == 2:
        pass  # TODO: Implement medium level AI
    elif level == 3:
        # Hard level: use Minimax with alpha-beta pruning to find the best move
        _, move = minimax(board, player, player, -np.inf, np.inf)
        return move


def minimax(board, player, current_player, alpha, beta):
    winner, winner_symbol = check_winner(board)
    if winner:
        if winner_symbol is None:
            return 0, None
        elif winner_symbol == player:
            return 1 if current_player == player else -1, None
        else:
            return -1 if current_player == player else 1, None

    if current_player == player:
        # Maximize score
        score = -np.inf
        best_move = None
        for move in get_possible_moves(board):
            new_board = make_move(board, move, player)
            child_score, _ = minimax(new_board, player, 3 - player, alpha, beta)
            if child_score > score:
                score = child_score
                best_move = move
            alpha = max(alpha, score)
            if beta <= alpha:
                break  # Beta cut-off
        return score, best_move
    else:
        # Minimize score
        score = np.inf
        best_move = None
        for move in get_possible_moves(board):
            new_board = make_move(board, move, 3 - player)
            child_score, _ = minimax(new_board, player, 3 - player, alpha, beta)
            if child_score < score:
                score = child_score
                best_move = move
            beta = min(beta, score)
            if beta <= alpha:
                break  # Alpha cut-off
        return score, best_move


def get_possible_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if board[i, j, k] == 0:
                    moves.append((i, j, k))
    return moves


def make_move(board, move, player):
    new_board = board.copy()
    new_board[move] = player
    return new_board


# Step 6: Determine level of difficulty for AI player
def get_ai_level():
    while True:
        try:
            level = int(input("Enter AI level (1=easy, 2=medium, 3=hard): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level, try again")
        except ValueError:
            print("the invalid input try again")
        # Step 7: Play the game
        # def play_game(): # Display welcome message print("Welcome to 3D Tic-Tac-Toe!") time.sleep(1)

        # Get level of difficulty for AI player
        ai_level = get_ai_level()
        time.sleep(1)

        # Display the board
        print("Here's the board:")
        display_board(board)
        time.sleep(1)

        # Choose player 1 (X) or player 2 (O) randomly
        player = np.random.choice([1, 2])
        print(f"Player {player} goes first.")
        time.sleep(1)

  # Play the game
def play_game():
    # Step 1: Create the board
    board = np.zeros((3, 3, 3))

    # Display welcome message
    print("Welcome to 3D Tic-Tac-Toe!")
    time.sleep(1)

    # Choose game type
    while True:
        game_type = input("Choose game type (1=human vs human, 2=human vs AI): ")
        if game_type == "1":
            player1, player2 = "X", "O"
            break
        elif game_type == "2":
            player1 = input("Choose player 1 (X) or let the computer choose randomly (R): ").upper()
            if player1 == "R":
                player1 = np.random.choice(["X", "O"])
            player2 = "X" if player1 == "O" else "O"
            break
        else:
            print("Invalid choice, try again")

    # Get level of difficulty for AI player
    if game_type == "2":
        ai_level = get_ai_level()
        time.sleep(1)

    # Display the board
    print("Here's the board:")
    display_board(board)
    time.sleep(1)

    # Choose player 1 (X) or player 2 (O) randomly
    current_player = np.random.choice([player1, player2])
    print(f"{current_player} goes first!")
    time.sleep(1)

    # Main game loop
    while True:
        # Get move from player
        if current_player == player1:
            print(f"It's {current_player}'s turn!")
            move = get_player_move()
        else:
            print(f"It's {current_player}'s turn (AI)!")
            move = get_ai_move(board, ai_level, 3 - int(player1 == "X"))

        # Make the move
        board = make_move(board, move, 1 if current_player == "X" else 2)
        display_board(board)

        # Check for a winner
        winner, winner_symbol = check_winner(board)
        if winner:
            if winner_symbol is None:
                print("It's a tie!")
            elif winner_symbol == "X":
                print("Player 1 (X) wins!")
            else:
                print("Player 2 (O) wins!")
            break

        # Switch players
        current_player = player1 if current_player == player2 else player2


# Ask if players want to play again
while True:
    try:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == 'y':
            board = np.zeros((3, 3, 3))
            play_game()
        elif play_again.lower() == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input, try again")
    except ValueError:
        print("Invalid input, try again")
    def main() -> object:
     play_game()

    if __name__ == '__main__':
        main()