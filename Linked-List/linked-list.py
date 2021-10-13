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
            element = self.head
            self.head = None
            self.length = 0
            return element.value
        
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp.value

    def prepend(self, value): # add an element to the first of the linkedlist
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        temp = self.head
        self.head = new_node
        self.head.next = temp
        self.length += 1


    def pop_first(self): # Pop an element from the beginning
        if self.length == 0:
            return None
        elif self.length == 1:
            element = self.head
            self.head = None
            self.length = 0
            return element

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp
    

    def get_value(self, index): # Get with index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    
    def set_value(self, index, value): # Set specified value at the exact index
        temp = self.get_value(index)
        if temp:
            temp.value = value
            return True
        return False
    

    def insert(self, index, value): # Insert with the index
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get_value(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    

    def remove(self, index): # Remove with the given index
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            return self.pop_first(index)
        elif index == self.length - 1:
            return self.pop()
        prev = self.get_value(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    

    def reverse(self):
        # Swapping head with tail
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None
        # Iterate through the list to reverse the order
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
