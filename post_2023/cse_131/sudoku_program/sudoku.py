import json

def main():
    # This function calls the necessary functions to run the game.
    board = read_board()
    print(board)
    display_board(board)


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
    return

def play_round(board):

    return

def parse_input(coordinate):

    return #row and column.

def is_input_legal(board, number, row, column):

    return #boolean variable true or false.


main()