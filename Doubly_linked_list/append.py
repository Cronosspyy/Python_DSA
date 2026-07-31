class node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class doubly_linked_list:
    def __init__(self,value):
        new_node = node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 
    
    def Print_my_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
  
  
    def append(self,value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = None
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 
        return True

dll = doubly_linked_list(7)
dll.append(4)
dll.Print_my_list()
