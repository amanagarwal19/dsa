class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in range(len(s)):
            ch = s[i]
            if(ch=='[' or ch=='{' or ch=='('):
                stack.append(ch)
            else:
                if(len(stack)==0):
                    return False
                else:
                    top = stack.pop() #pop element to view as peek
                    if  ((top == '[' and ch!=']') or 
                        (top == '(' and ch!=')') or
                        (top == '{' and ch!='}')):
                            return False;
                    
        if(len(stack)!=0):
            return False
        return True;