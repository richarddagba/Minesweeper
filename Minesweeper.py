# imports the random module to generates random mines on the board.
import random

class Minesweeper:                     # defines a class called Minesweeper to represent the game
    def __init__(self, n, k):          # defining a constructor for the Minesweeper class that takes two arguments, n being the size of the board and k being the mines to be inserted
       # initializing instance variables to store the size of the board, number of mines,layout of the board n rows by n cloumns with all cells marked with '#'
        self.n = n
        self.k = k
        self.board = [['#' for i in range(n)] for j in range(n)]
        self.mines = self.generate_mines()           # random generation of k mines
        
    def generate_mines(self):   # method to generate k random mines
        mines = []              # creating an empty list to store mines
      # looping until k unique mines have been generated and adding new mines that arent present  
        while len(mines) < self.k:
            mine = (random.randint(0, self.n-1), random.randint(0, self.n-1))
            if mine not in mines:
                mines.append(mine)
        
        # returning list of generated mines
        return mines
    
    def render_board(self):               # defining a method to render the current state of board
        print(' ', ' '.join([str(i) for i in range(1, self.n+1)]))       # Printing the column numbers as headers
        # Loop through rows of the board and storing the current row as a variable.
        for i in range(self.n):
            row = self.board[i]
        # Print the row letter as a header and join the cells of the current row with spaces
   
            print(chr(65+i), ' '.join(row))
    
    def reveal_field(self, field):             # Defining a method to reveal a field on the board
        row, col = ord(field[0].upper()) - 65, int(field[1:]) - 1 # Parsing the user input of a field to reveal
        if (row, col) in self.mines:
        # Checking if the revealed field is a mine and printing a message if it is   
            print('Game Over! You lost!')      
            return False
        
        # Counting the amount of nearby mines and recursively revealing all surrounding non-mine fields if the revealed field is not a mine. Setting the revealed field to '0' and repeatedly revealing all surrounding fields if the number of nearby mines is zero. Alternatively, adjusting the exposed field to the number of nearby mines
        
        else:
            mine_count = 0               # mine_count is initialized to zero
         # ensure loop does not go beyond the bounds of the gameboard   
            for i in range(max(0, row-1), min(row+2, self.n)):
                for j in range(max(0, col-1), min(col+2, self.n)):
         # checks if a cell contains a mine and mine_count is incremented if it does           
                    if (i, j) in self.mines:
                        mine_count += 1
        # set row and column to zero if the mine_count is zero
            if mine_count == 0:
                self.board[row][col] = '0'
                for i in range(max(0, row-1), min(row+2, self.n)):
                    for j in range(max(0, col-1), min(col+2, self.n)):
        # if revealed field isnt a mine, check adjacent mines and reveal all non-mine cells around it.               
                        if self.board[i][j] == '#':
                            self.reveal_field(chr(65+i) + str(j+1))
            else:
                self.board[row][col] = str(mine_count)
            if self.check_win():
                print('Congratulations! You won!')
                return False
            return True
   # check if game has been won by checking cells on the board 
    def check_win(self):
        for i in range(self.n):
            for j in range(self.n):
   # if a cell is still hidden and does not  contain a mine, the game isnt won yet. If all hidden cells contain mines, then the game has been won.            
                if self.board[i][j] == '#' and (i, j) not in self.mines:
                    return False
        return True
# check if script is being run as the main program. if it is, 
# prompts user for the size of board and number of mines.
# if the input is invalid, the user is prompted again until valid inputs are provided.
if __name__ == '__main__':
    n, k = 0, 0
    
    while n <= 0 or k <= 0 or k >= n**2:
        try:
            n = int(input('How big should be the gameplay be(n)? '))
            k = int(input('How many mines would you like to find (k)? '))
            
    
            if k >= n**2:
                print('Invalid number of mines!')
                n, k = 0, 0
            if n <= 0:
                print ("That's not a valid number for the dimension!")
        except ValueError:
            print('Invalid input!')
    # Object 'minesweeper' is created and initial gameboard is displayedonce valid iputs are entered.
    game = Minesweeper(n, k)
    game.render_board()
    while True:
        field = input('What field to reveal? ') # user is prompted to selet cell to show its content
        if not game.reveal_field(field):
            game.render_board()
            break
        game.render_board()