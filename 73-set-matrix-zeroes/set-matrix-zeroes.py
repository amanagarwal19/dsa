class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row0 = -1

        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    matrix[0][j]=0
                    if(i==0):
                        row0=0
                    else:
                        matrix[i][0]=0
        print(row0)
        # Update from 1,1 --> m,n 
        for i in range(1,m):
            for j in range(1,n):
                if(matrix[i][0]==0 or matrix[0][j]==0):
                    matrix[i][j]=0
        print(matrix)

        # Important to update 0th column firsts
        # or else matrix[0][0] maynot have right value if 
        # row0's value updates 0th row in next loop
        
        # Update first col
        if(matrix[0][0]==0):
            for i in range(m):
                matrix[i][0]=0
        
        # Update first row
        if(row0==0):
            for j in range(n):
                matrix[0][j]=0

