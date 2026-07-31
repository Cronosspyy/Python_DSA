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
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True
    
    def pop_first(self):
        if self.length==0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length==0:
            self.tail = None
        return temp.value ## gives value of temp
  
    def get(self,index):
        if index < 0 or index>= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value
  
    def set_value(self,index,value):
        if index < 0 or index>= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
  
    def insert(self,value,index):
        new_node = Node(value)

        if index<0 and index>=self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
        
        

my_linked = LinkedList(0)
my_linked.append(1)
my_linked.append(2)
my_linked.append(3)

my_linked.print_list()

print("         ")  
my_linked.insert(4,4)
my_linked.insert(56,2)
my_linked.insert(-1,0)

my_linked.print_list()
