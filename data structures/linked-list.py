class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Returns true if linked list is empty
        """
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the linked list object
        """
        current_node = self.head
        count = 0

        while current_node:
            count += 1
            current_node = current_node.next_node

        return count

    def prepend(self, data):
        """
        Adds new data node at the beginning of the list
        Has O(n) runtime
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
