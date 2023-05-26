import json

def main():
    """
    This function calls all the necessary functions to run the game.
    """
    # Set variables.
    board = read_board()
    quit_game = "no"
    continue_game = True
    # Begin game.
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
    """
    Purpose of read_board is to read the board into a list of lists.
    """
    board_name = input("What is the name of the board? ")
    with open(board_name) as file:
        board_file = json.load(file)
        board_list = []
        # Iterate through json file and append each list to a variable called board_list.
        for line in board_file["board"]:
            board_list.append(line)

    return board_list

def display_board(board):
    """
    This function displays the board to the user.
    """
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
            # If the loop is at the beginning of a row, then print the current row number.
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
    """
    This function saves the board to a file.
    """
    save_file = open("current_board.json", "w")
    board_dictionary = {
        "board" : board
    }
    json.dump(board_dictionary, save_file)
    save_file.close()

    return board

def play_round(board):
    """
    This function plays one round of the game.
    """
    finished_round = False
    while finished_round != True:
        # Get the coordinate from the user.
        column, row, coordinate = get_coordinate(board)
        # If the player inputs "Q" then quit and save.
        if column == "Q":
            finished_round = True
            return board, "quit"
        # Otherwise, get the value from the user.
        else:
            value = get_value(board, coordinate, column, row)

            # IF VALUE = A NUMBER. THEN USE THE COORDINATE AND THE VALUE TO UPDATE THE BOARD 
            # BECAUSE IT'S CORRECT. 
            if type(value) == int:
                board[row][column] = value
                finished_round = True
            # IF VALUE = NULL. THEN THE GUESS DIDN'T FOLLOW THE RULES OF SUDOKU, AND GO BACK TO THE 
            # START OF THE WHILE LOOP.
            if value == None:
                finished_round = False
            
            

    return board, "no"

def get_coordinate(board):
    """
    This function gets the coordinate from the user, error checks the user input, and returns a column and row.
    """
    # Set variables.
    is_input_valid = False
    is_coordinate_valid = True
    column_valid = False
    row_valid = False
    done = False

    # Get coordinate from user. We use a sentinel-controlled loop for this.
    while done != True:
        coordinate = input("Specify a coordinate to edit or 'Q' to save and quit ")
        if coordinate.upper() == "Q":
            done = True

            return "Q", 0, 0
        
        elif coordinate.upper() == "S":
            print("Which square would you like possible values for? ")

        # Error check user input.
        for character in coordinate.upper():
            if "A" <= character <= "Z":
                column = ord(character) - ord("A")
                column_valid = True
            elif 1 <= int(character) <= 9:
                row = int(character) - 1
                row_valid = True
            else:
                is_input_valid = False
                print(f"ERROR: Square {coordinate} is invalid. ")

        # is_input_valid is the controlling expression. It must be true to leave the loop.
        if column_valid == True and row_valid == True:
            is_input_valid = True


        if is_input_valid:
        # Finished getting coordinate. Now check if coordinate is filled.
            selected_coordinate = board[column][row]
            if selected_coordinate == " ":
                is_coordinate_valid = True
            else:
                is_coordinate_valid = False
                print(f"ERROR: Square {coordinate} is filled. ")
                
            
            if is_input_valid == True and is_coordinate_valid == True:
                done = True

    return column, row , coordinate.upper()

def get_value(board, coordinate, column, row):
    """
    Get value does two things. It gets the value from the user, and it calls check_rules() to see if the user input follows sudoku's rules.
    """
    # Part 1. Validate input.
    valid = False
    while valid == False:
        value = input(f"What value goes in {coordinate}? ")
        for character in value:
                if "A" <= character.upper() <= "Z":
                    valid = False
                    print("ERROR: Value must be an integer. ")
                    
                elif 1 <= int(value) <= 9:
                    valid = True
                elif value <1 or int(value) > 9:
                    print("The value must be between 1 and 9. ")
                else:
                    valid = False
                    print(f"ERROR: Square {coordinate} is invalid. ")

    # Part 2. Check if the input follows sudoku rules.
    
    follows_rules = check_rules(board, int(value), column, row)

    if follows_rules:
        return int(value)

    elif follows_rules == False:
        return 


def check_rules(board, value, column, row):
    """
    This function checks if the guess can FIT. It DOES NOT check if the guess is correct.
    """
    # Check if the number already exists in row.
    for i in range(9):
        row_checker = board[row][i]
        if row_checker == value:
            print(f"The number, {value} is already in this row.")
            return False
    # Check if the number already exists in column.
    for i in range(9):
        column_checker = board[i][column]
        if column_checker == value:
            print(f"The number, {value} is already in this column.")
            return False
    # Check if the number already exists in box.
    box_x = column // 3
    box_y = row // 3
    for i in range(box_y*3, box_y*3 + 3):
        for x in range(box_x*3, box_x*3 +3):
            if board[i][x] == value and (i,x) != (row, column):
                print(f"The number, {value} is already in this box. ")
                return False

    return True

main()