stock_prices = []

stock_prices.append(234.35)  # index 0
stock_prices.append(46.36) # index 1
stock_prices.append(245.00) # index 2
stock_prices.append(123.46) # index 3


stock_prices.insert(1, 100.50)


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        
        current = self.head
        while current.next:
            current = current.next
            
        current.next = Node(data, None)
        
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        
        return count
    
    def insert_at(self, position, data):
        if position < 0 or position >= self.get_length():
            raise Exception("Invalid index")
        
        if position == 0:
            self.insert_at_beginning(data)
        
        index = 0
        current = self.head
        while current:
            if index == position - 1:
                node = Node(data, current.next)
                current.next = node
                break
            current = current.next
            index += 1
            
    def remove_at(self, position):
        if position < 0 or position >= self.get_length():
            raise Exception("Invalid index")
       
        if position == 0:
            self.head = self.head.next
    
        index = 0
        current = self.head
        while current:
            if index == position - 1:
                current.next = current.next.next
                break
            current = current.next
            index += 1
                

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        current = self.head
        linked_list_string = ''
        
        while current:
            linked_list_string += str(current.data) + '-->'
            current = current.next
            
        print(linked_list_string)
        
    # Method 1: insert_after_value
    # def inser_after_value(self, data_after, data_to_insert)
    #  - Check for a value in our linked list and insert a node after the node that hosts that value
    #  - if not value matches whatever value you are seacrching for, just print value not found
    
    # Method 2: remove_by_value
    # def remove_by_value(self, data_to_remove)
    #  - Checks for a node with a value passed then removes that node in the linked list
    #  - if no value is found, just print value not found
        

linked_list = LinkedList()
linked_list.insert_at_beginning(234.35)
linked_list.insert_at_beginning(46.36)
linked_list.insert_at_beginning(245.00)
linked_list.insert_at_beginning(100.50)
linked_list.print()

linked_list.remove_at(2)
linked_list.print()

linked_list.insert_at(2, 250.54)
linked_list.print()

linked_list.insert_at_end(1000.3)
linked_list.print()
print(linked_list)

