class MinStack:
    list1=[]
    list2=[]
    def __init__(self):
        self.list1=[]
        self.list2=[]
        return None

    def push(self, val: int) -> None:
        self.list1.append(val)
        n = len(self.list2);
        if(n==0):   #no item in stack to store mins
            self.list2.append(val)
        elif(val <= self.list2[n-1]): # imp to have = 
            self.list2.append(val)

    def pop(self) -> None:
        item = self.list1.pop()
        if(item == self.list2[len(self.list2)-1]): #popping min element
            self.list2.pop()

    def top(self) -> int:
        return self.list1[len(self.list1)-1]

    def getMin(self) -> int:
        return self.list2[len(self.list2)-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()