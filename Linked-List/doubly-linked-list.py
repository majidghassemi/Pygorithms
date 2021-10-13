# Creating a Node class in order to use it in our linked-list
# DLL = Doubly Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList: # Create our DLL constructor and initalize it
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    
    def print_list(self): # Helper function to print our linked list in a right sequence
        temp = self.head
        while temp.next is not None:
            print(temp.value)
            temp = temp.next


    def append(self, value): # Append an element at the end of our DLL
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    

    def pop(self): # Pop an element from the DLL - Last element
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
        return temp

    def prepend(self, value): # add an element to the first of the DLL
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True