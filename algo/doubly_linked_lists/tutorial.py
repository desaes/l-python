class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedLists:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # this operation inserts items at the end of the linked lists
    # so we have to manipulate the tail node in O(1) running time
    def insert(self, data):

        new_node = Node(data)

        # when list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # there is at least 1 item in the data structure
        # we keep inserting items at the end of the linked list
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse_forward(self):
        actual_node = self.head
        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):
        actual_node = self.tail
        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.previous

if __name__ == '__main__':
    linked_list = DoublyLinkedLists()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.traverse_forward()
    linked_list.traverse_backward()