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

dll = doubly_linked_list(7)
dll.Print_my_list()
