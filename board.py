## board and tile setup

board = [ ## id borad that has a row that is loop into
    "Go", 
    "property 1",
    "chance", 
    "property 2", 
    "jail",## tiles
    "property 3", 
    "free parking", 
    "property 4", 
    "Go to jail", 
    "property 5"
]

def real_board(board):
    print("Board and tiles")
    for p,in range(board): ## looping throug
        print(f"{i}: {board[p]}")

real_board(board) ## calling out the board 

