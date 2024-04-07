class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row0=[None]*n
        col0=[None]*m

        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    row0[j] = 0;
                    col0[i] = 0;

        for j in range(n):
            if(row0[j]==0):
                for i in range(m):
                    matrix[i][j] = 0;
        
        for i in range(m):
            if(col0[i]==0):
                for j in range(n):
                    matrix[i][j]=0;


        