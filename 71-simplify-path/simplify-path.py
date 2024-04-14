class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        n = len(path)
        #Split on '/'

        dirs = path.split('/')
        print(dirs)
        for i in range(len(dirs)):
            curr = dirs[i]
            if(curr == '..'):
                if(len(stack)!=0):
                    stack.pop()
            elif(curr=='' or curr == '.'):
                continue
            else:
                stack.append(curr)

        ans = "/"
        for i in range(len(stack)):
            ans = ans + stack[i]
            if(i!=len(stack)-1):
                ans = ans + "/"
        return ans