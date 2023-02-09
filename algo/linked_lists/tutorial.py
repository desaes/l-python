class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None
        
    def __repr__(self) -> str:
        return str(self.data)
    
class LinkedList:
    def __init__(self) -> None:
        # this is the first node of the linked list
        # WE CAN ACCESS THIS NODE EXCLUSIVELY !!!
        self.head = None
        self.num_of_nodes = 0

    # O(1) constant running time
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # the head is NULL (so the data structure is empty)
        if self.head is None:
            self.head = new_node
        else: 
            new_node.next_node = self.head
            self.head = new_node

    # O(N)
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # check if the linked list is empty
        if self.head is None:
            self.head = new_node
        else:
            # when the linked list is not empty
            actual_node = self.head

            # this is why it has O(N) linear running time
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            # actual_node is the last none: so we insert the new_node
            # right after the actual node
            actual_node.next_node = new_node


    # O(1)
    def size_of_list(self):
        return self.num_of_nodes
    
    # O(N)
    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

    # O(N)
    def remove(self, data):
        if self.head is None:
            return 
        
        actual_node = self.head
        # we have to track the previous node for future pointer updates
        # this is why doubly linked lists are better - we can get the previous
        # node (here with linked lists it is impossible)
        previous_node = None

        # search for the item we want to remove (data)
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # search miss
        if actual_node is None:
            return
        
        # update the references (so we have the data we want to remove)
        # the head node is the one we want to remove because previous_node was
        # initialized with None and search stopped on first item
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            # remove an internal node by updating the pointers
            # NO NEED TO del THE NODE BECAUSE THE GARBAGE COLLECTOR WILL DO THAT
            previous_node.next_node = actual_node.next_node





if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_start(10)
    linked_list.insert_start('Adam')
    linked_list.insert_start(7.5)
    linked_list.insert_end(9)
    linked_list.remove('Adam')
    linked_list.traverse()