class Solution:

    def dfs(self,board: List[List[str]], i, j,visited,word:str,m,n,idx):

        if(idx == len(word)):
            return True;

        if(i<0 or i>=m or j<0 or j>=n):
            return False;

        if(visited[i][j]==True):
            return False;

        if(board[i][j]!=word[idx]):
            return False;
       
        visited[i][j] = True;
        c1 = self.dfs(board,i+1,j,visited,word,m,n,idx+1);
        c2 = self.dfs(board,i,j+1,visited,word,m,n,idx+1);
        c3 = self.dfs(board,i-1,j,visited,word,m,n,idx+1);
        c4 = self.dfs(board,i,j-1,visited,word,m,n,idx+1);
        visited[i][j] = False;
        return c1 or c2 or c3 or c4

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                visited = [[False for p in range(n)] for l in range(m)]
                if (self.dfs(board,i,j,visited,word,m,n,0)):
                    return True;

        return False;