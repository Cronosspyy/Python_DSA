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
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1 
        return temp.value
   
   
    def prepend(self,value):
        new_node = node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1 
        return temp



dll = doubly_linked_list(1)
dll.prepend(0)
dll.append(2)
dll.Print_my_list()
dll.pop_first()
dll.Print_my_list()
