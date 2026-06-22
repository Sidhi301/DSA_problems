class MinStack(object):

    def __init__(self):
        self.arr=[]
        self.min_arr=[]
    def push(self, value):
        self.arr.append(value)
        if  not self.min_arr or value<=self.min_arr[-1]:
            self.min_arr.append(value)
        return "null"
    def pop(self):
        if not self.arr:
            return "null"
        val= self.arr.pop()
        if val == self.min_arr[-1]:
            self.min_arr.pop()
        return val
        

    def top(self):
        if not self.arr:
            return "null"
        return self.arr[-1]
        
        

    def getMin(self):
        return self.min_arr[-1]
        
        
       
        

     
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()