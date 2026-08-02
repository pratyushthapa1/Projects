import random

def menu():
    """
    Display the menu options and get user input.
    """
    print("Choose from the following options.")
    print("1. Play a game")
    print("2. Save your score to leaderboard")
    print("3. Load and display leaderboard")
    print("q. Quit or leave the game")

    # Get user input
    choice = input("Enter your choice (1, 2, 3, or q): ").strip().lower()

    while choice not in ['1', '2', '3', 'q']:
        print("Invalid choice. Please enter 1, 2, 3, or q.")
        choice = input("Enter your choice (1, 2, 3, or q): ").strip().lower()

    return choice

def getPlayerName():
     print("Welcome to Tic Tac Toe!")
     player = input("Enter your name: ").strip().lower()
     return player

def load_scores():
    """
    Load the leaderboard scores from the file 'leaderboard.txt'.
    Return the scores in a Python dictionary.
    """
    scores = {}  # Initialize an empty dictionary to store scores

    # Attempt to open the file and read its contents
    try:
        with open('leaderboard.txt', 'r') as file:
            for line in file:
                # Split each line into player name and score
                player, score = line.strip().split(',')
                scores[player] = int(score)  # Add player and score to the dictionary
    except FileNotFoundError:
        print("Leaderboard file not found.")
    except Exception as e:
        print("An error occurred while loading scores:", e)

    return scores

def save_scores(scores):
    """
    Save the leaderboard scores to the file 'leaderboard.txt'.
    """
    try:
        with open('leaderboard.txt', 'w') as file:
            for player, score in scores.items():
                file.write(f"{player},{score}\n")
        print("Scores saved to leaderboard successfully.")
    except Exception as e:
        print("An error occurred while saving scores:", e)

def initialise_board(board):
    """
    Set all elements of the board to one space ' '.
    """
    for row in range(3):
        for col in range(3):
            board[row][col] = ' '

def draw_board(board):
    """
    Draw the noughts and crosses board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def welcome(board):
    """
    Print the welcome message and display the board by calling draw_board(board).
    """
    print("Welcome to Tic Tac Toe!\nThe board layout is shown below:")
    draw_board(board)

def get_player_move(board):
    """
    Ask the user for the cell to put the X in, and return row and col.
    """
    while True:
        try:
            # Ask the user for row and column numbers
            row = int(input("Enter the row number (0, 1, 2): "))
            col = int(input("Enter the column number (0, 1, 2): "))
            
            # Check if the cell is empty
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Please choose an empty cell within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_computer_move(board):
    """
    Let the computer choose a cell to put a nought in and return row and col.
    """
    while True:
        # Generate random row and column numbers
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        
        # Check if the selected cell is empty
        if board[row][col] == ' ':
            return row, col

def check_for_win(board, mark):
    """
    Check if either the player or the computer has won.
    Return True if someone won, False otherwise.
    """
    # Check rows for a win
    for row in board:
        if all(cell == mark for cell in row):
            return True

    # Check columns for a win
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    # If no winning condition is found, return False
    return False

def check_for_draw(board):
    """
  Look for a draw when the game is over.
    In case a draw occurs, return True; if not, return False.
    """
    for row in board:
        if ' ' in row:
            return False 
    return True 

def play_game():
    # Create the board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # Initialize the board
    initialise_board(board)

    # Call the welcome function
    welcome(board)

    # Game loop
    while True:
        # Get the player's move
        row, col = get_player_move(board)
        board[row][col] = 'X'  # Update the board with player's move
        draw_board(board)

        # Check if the player wins
        if check_for_win(board, 'X'):
            print("Congratulations! You win!")

            break

        # Check for a draw
        if check_for_draw(board):
            print("It's a draw!")
            break

        # Get the computer's move
        print("Computer's move:")
        comp_row, comp_col = choose_computer_move(board)
        board[comp_row][comp_col] = 'O'  # Update the board with computer's move
        draw_board(board)

        # Check if the computer wins
        if check_for_win(board, 'O'):
            print("Sorry! Computer wins!")
            break

        # Check for a draw again
        if check_for_draw(board):
            print("It's a draw!")
            break

def main():
    playerName = getPlayerName()
    while True:
        user_choice = menu()
        scores = load_scores()
       
        if user_choice == '1':
            play_game()
        elif user_choice == '2':
            # Placeholder for saving score function call
            
            if playerName in scores:
                scores[playerName] += 1
            else:
                scores[playerName] = 1
            
            save_scores(scores) 
            print("score saved")

        elif user_choice == '3':
            # Placeholder for loading leaderboard function call
            print("Leaderboard Scores:")
            for player, score in scores.items():
                print(f"{player}: {score}")
        elif user_choice == 'q':
            print("Quitting the game.")
            break  # Exit the loop and end the program

main()
