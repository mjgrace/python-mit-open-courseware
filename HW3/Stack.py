class Stack:
    def __init__(self):
        self.list = []
        
    def push(self,obj):
        self.list.insert(0, obj)
    
    def pop(self):
        if (len(self.list) == 0):
            return ""
        else:
            return self.list.pop(0)