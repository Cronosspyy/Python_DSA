class Node:
    def __init__(self,value):
        self.value=value
        self.next = None

class LinkedList:
    def __init__(self,value=None):
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head=None
            self.tail = None
            self.length = 0
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 
    
    def pop(self):
        if self.length==0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length ==0:
            self.head = None
            self.tail = None
        return temp.value
        

my_linked = LinkedList(1)
my_linked.append(2)
my_linked.append(3)
print(my_linked.pop())
print(my_linked.pop())
print(my_linked.pop())
print(my_linked.pop())