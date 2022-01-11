'''
Tic-Tac-Toe: A Solution
Author: Bro. Manley
'''

'''
Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.
'''

def main():
    #calls player function
    player = next_player("")
    #calls board fucntion
    board = create_board()
    #3.Players take turns putting their marks in empty squares.
    #The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
    #If all nine squares are full and neither player has three in a row, the game ends in a draw.
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("You did very well! Thanks for playing :) ") 

#creates a create_board function
def create_board():
    board = []
    for square in range():
        board.append(square + 1)
    return board

#displays board
def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def is_a_draw(board):
    #stops at 8
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def has_winner(board):
    return (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6])

def make_move(player,board):
    square = int(input(f"{player}'s turn to choose (1-9):"))
    board[square - 1]=player

#2.Player one uses x's. Player two uses o's.
def next_player(current):
    if current == "" or current =="o":
        return "x"
    elif current =="x":
        return "o"
    
#execute main function which contains all the functions
if __name__ == "__main__":
    main()

#How did you use a version control system to develop the programs?
#I used git clone to create a local copy of a project that already exits remotely on Visual Studio Code (VSC)
#On the command prompt I used cd [directory's name] to change directory
#I added the folder and used git add
#Checked the status of the file with  "git status"
#Typed git commit and then git push
