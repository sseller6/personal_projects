import json

def main():
    # Set variables
    board = read_board()
    quit_game = "no"
    continue_game = True
    # Begin game
    display_board(board)
    while continue_game:
        updated_board, quit_game = play_round(board)
        if quit_game == "quit":
            print("Your game is saved. Thank you for playing.")
            continue_game = False
        else:
            display_board(updated_board)
        
    write_board(updated_board)



def read_board():
    # Purpose of read_board is to read the board into a list of lists.
    with open("current_board.json") as file:
        board_file = json.load(file)
        board_list = []
        # Iterate through and 
        for line in board_file["board"]:
            board_list.append(line)

    return board_list

def display_board(board):
    # This function displays the board to the user.
    print("   A B C   D E F   G H I")
    column_count = 0
    # If the current row is the third or 6th row, then print the border.
    for row in range(0, 9):
        if row == 3 or row == 6:
            print("   ------+-------+------")
        # Find empty spots (0) and relace them with an empty string.
        for column in range(0, 9):
            if board[row][column] == 0:
                board[row][column] = " "
            # If the loop is at the beginning of a row, then print the current row number
            if column == 0:
                column_count += 1
                print(f"{column_count}| ", end="")
            # Since the sudoku board is divisible by three, we can use math to find out if the current column needs to have a divider right after it.
            if column % 3 == 0 and column != 0:
                print("| ", end="")
            if column == 8:
                print(board[row][column])
            else:
                print((str(board[row][column])) + " ", end="")

def write_board(board):
    # This function saves the board to a file.
    save_file = open("current_board.json", "w")
    board_dictionary = {
        "board" : board
    }
    json.dump(board_dictionary, save_file)

    save_file.close()
    return board

def play_round(board):
    finished_round = False
    while finished_round != True:
        # Get the coordinate from the user.
        column, row = get_coordinate(board)
        # If the player inputs "Q" then quit and save.
        if column == "Q":
            finished_round = True
            return board, "quit"
        # Otherwise, get the value from the user.
        else:
            value = get_value(board)
            finished_round = True
            # Use the coordinate and the value to update board.
            board[row][column] = value

    return board, "no"

def get_coordinate(board):
    is_input_valid = False
    is_coordinate_valid = True
    column_valid = False
    row_valid = False
    done = False
    coordinate = input("Specify a coordinate to edit or 'Q' to save and quit ")

    while done != True:
        if coordinate.upper() == "Q":
            done = True
            return "Q", 0
        for character in coordinate.upper():
            if "A" <= character <= "I":
                column = ord(character) - ord("A")
                column_valid = True
            elif 1 <= int(character) <= 9:
                row = int(character) - 1
                row_valid = True
            else:
                is_input_valid = False
                print(f"ERROR: Square {coordinate} is invalid. ")
        if column_valid == True and row_valid == True:
            is_input_valid = True
        # Finished getting coordinate. Now move on to getting value.
        selected_coordinate = board[column][row]
        if selected_coordinate == " ":
            is_coordinate_valid = True
        else:
            is_coordinate_valid = False
            print(f"ERROR: Square {coordinate} is filled. ")
            return
        
        if is_input_valid == True and is_coordinate_valid == True:
            done = True

    return column, row

def get_value(board):
    # Get value does two things. It gets the value from the user, and it checks the game rules. However, this week we won't worry about the game rules.
    # Part 1. Validate input.
    value = int(input('What number goes in B2? '))
    valid = False
    while valid == False:
        if 1 <= value <= 9:
            valid = True
            return value
        elif value <1 or value > 9:
            value = int(input("The value must be between 1 and 9. "))
        else:
            value = int(input("The value must be an integer. "))
    # Part 2. Verify rules (to-do for next week.)


main()