class Solution:
    def isAlive(self,board:List[List[int]], i,j):
        m = len(board)
        n = len(board[0])

        if i<0 or j<0 or i>=m or j>=n:
            return False
        # -1 means it was alive but is now dead
        if board[i][j] == 1 or board[i][j]==-1:
            return True
    
    def neighbourCount(self,board:List[List[int]],i,j):
        count=0
        if self.isAlive(board,i-1,j):    count = count+1
        if self.isAlive(board,i-1,j-1):  count = count+1
        if self.isAlive(board,i,j-1):    count = count+1
        if self.isAlive(board,i+1,j-1):  count = count+1
        if self.isAlive(board,i+1,j):    count = count+1
        if self.isAlive(board,i+1,j+1):  count = count+1
        if self.isAlive(board,i,j+1):    count = count+1
        if self.isAlive(board,i-1,j+1):  count = count+1
        return count

    

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # -1 : [1] -> [0]
        # +2 : [0] -> [1]
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                count = self.neighbourCount(board,i,j)
                if board[i][j] == 1: #live cell
                    if count < 2:
                        board[i][j] = -1
                    if count > 3:
                        board[i][j] = -1
                elif board[i][j] == 0: #dead cell
                    if count == 3:
                        board[i][j] = 2 #becomes live

        for i in range(m):
            for j in range(n):
                if(board[i][j]==-1): #supposed to be dead
                    board[i][j] = 0
                elif board[i][j]==2:
                    board[i][j] = 1 #becomes live
