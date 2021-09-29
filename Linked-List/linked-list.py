# Creating a Node class in order to use it in our linked-list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value): # Create our constructor and initalize it
        new_node = Node(value)
        self.value = value
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_values(self): # Helper function to print our linked list in a right sequence
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value): # Append an element at the end of linked list
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self): # Pop an element from the linkedlist - Last element
        if self.length == 0:
            return None
        elif self.length == 1:
            element = self.head.value
            self.head = None
            self.head.next = None
            self.length == 0
            return element
        
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp.value

    def prepend(self, value): # add an element to first of the linkedlist
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        temp = self.head
        self.head = new_node
        self.head.next = temp
        self.length += 1

