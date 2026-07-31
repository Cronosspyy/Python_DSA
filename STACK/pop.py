class Node:
    def __init__(self,value):
        self.value= value
        self.next = None

class stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def Print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def Push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1 
        return True
    
    def pop(self):
        temp = self.top
        if self.height == 0:
            return None
        else:
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp.value
    



stk = stack(4)
stk.Push(5)
stk.Push(6)

stk.Print_stack()

print('popped itme is',stk.pop(),"\n")

print("after pop stack is ")

stk.Print_stack()
print("top value is:",stk.top.value)