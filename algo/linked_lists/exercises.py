class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def insert(self, data) -> None:
        self.size += 1
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def traverse(self) -> None:
        actual_node = self.head
        while actual_node != None:
            print(actual_node.data)
            actual_node = actual_node.next

    def middle(self) -> None:
        a, b = self.size // 2, self.size % 2

        if b > 0:
            actual_node = self.head
            i = 1
            while i < a + b:
                actual_node = actual_node.next
                i += 1
            print(actual_node.data)
        else:
            print('linked list has an even number of elements')

    # in this approach, we will have 2 pointers. 
    # First pointer will traverse the list one node at a time
    # Second pointer will traverse the list two nodes at a time
    # When the faster pointer reaches the end of the list
    # then the slower pointer is pointing to the middle node
    def middle2(self) -> Node:
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.next and fast_pointer.next.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        return(slow_pointer)
    
    def reverse(self) -> None:
        actual_node = self.head
        
        
        while actual_node:
            last_node = actual_node
            actual_node = actual_node.next
        
        

        

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.traverse()
    print(ll.middle2().data)
    ll.reverse()
    ll.traverse()

