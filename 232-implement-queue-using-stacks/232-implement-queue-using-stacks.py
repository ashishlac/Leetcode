class MyQueue(object):
    myQueue=[]
    def __init__(self):
        self.stack1 = []
        
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.stack2=[]
        temp=self.stack1[0]
        print(temp,self.stack1)
        for i in range(1,len(self.stack1)):
            self.stack2.append(self.stack1[i])
        self.stack1 = self.stack2
        return temp
    
    def peek(self):
        """
        :rtype: int
        """
        return self.stack1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()