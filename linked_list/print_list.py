class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value) #yeh value node me jaegi 
        self.head = new_node # head ko new node pr point kr rhe hai 
        self.tail = new_node 
        self.lenght = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
linkedlist_obj1 = LinkedList(4)
print(linkedlist_obj1.head.value) #value fetch kr rhe h using header kyuki 1st element h 
linkedlist_obj1.print_list()