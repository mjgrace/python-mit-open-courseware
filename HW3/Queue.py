class Queue:
    def __init__(self):
        self.list = []
        
    def insert(self,obj):
        self.list.append(obj)
    
    def remove(self):
        if (len(self.list) == 0):
            return ""
        else:
            return self.list.pop(0)