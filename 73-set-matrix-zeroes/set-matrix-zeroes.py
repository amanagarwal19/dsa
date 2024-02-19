class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        col0 = -1

        # set top row as 0 for columns marking
        # set left column as 0 for row marking
        # use col0 to address the 0th column
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j==0:
                        col0=0
                    else:
                        matrix[0][j]=0

        # fill from (1,1) to (m-1,n-1)
        # So that we dont modify the top row/column
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j]==0:
                    matrix[i][j]=0

        # fill the first row based on [0][0]
        if(matrix[0][0]==0):
            for j in range(0,n):
                matrix[0][j] = 0
        
        # fill the first column based on col0 variable
        if(col0==0):
            for i in range(m):
                matrix[i][0] = 0

        