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
    

    def pop_first(self): # Pop an element from the beginning of DLL
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
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
    

    def get(self, index): # Get specified value with index
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    
    def set_value(self, index, value): # Set specified value at the exact index
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    

    def insert(self, index, value): # Insert value at the specified index
        if index < 0 or index > self.length:
            return False or None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True


    def remove(self, index): # Remove an element with the given index
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        before = self.get(index - 1)
        temp = before.next
        after = self.get(index + 1)
        before.next = after.prev
        after.prev = before.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

        