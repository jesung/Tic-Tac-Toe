import numpy as np

class tic_tac_toe:
    def __init__(self):
        self.board = np.array([[2,2,2],[2,2,2],[2,2,2]])
        self.turn = 0

    def reset(self):
        self.board = np.array([[2,2,2],[2,2,2],[2,2,2]])
        self.turn = 0

    def move(self,x,y):
        self.board[x,y] = self.turn
        
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0

    def win(self):
        for i in range(3):
            if self.board[0,i]==self.board[1,i]==self.board[2,i]<2:
                return 'Won'
            if self.board[i,0]==self.board[i,1]==self.board[i,2]<2:
                return 'Won'

        if self.board[0,0]==self.board[1,1]==self.board[2,2]<2:
            return 'Won'
        if self.board[0,2]==self.board[1,1]==self.board[0,2]<2:
            return 'Won'

        if not 2 in self.board:
            return 'Drawn'
        else:
            return 'In-Progress'

def move_gen(board_state, turn):
    legal_moves = {}
    
    for i in range(3):
        for j in range(3):
            if board_state[i,j] == 2:
                tmp_board = board_state.copy()
                tmp_board[i,j] = turn
                legal_moves[(i,j)]=tmp_board.flatten()

    return legal_moves
    
