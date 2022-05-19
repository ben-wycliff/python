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

    def search(self, key):
        """
        Searches for the first node that contains data that matches the key
        Takes O(n) runtime
        """
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return current_node
            current_node = current_node.next_node
        return None

    def insert(self, index, data):
        """
        Inserts new data node at specified index
        Takes O(n) at worst case and O(1) for 0 index
        """
        new_node = Node(data)
        current_node = self.head
        position = index

        if index == 0:
            self.prepend(data)

        if index > 0:
            while position > 1:
                current_node = current_node.next_node
                position -= 1

            prev_node = current_node
            next_node = current_node.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, key):
        """
        Removes first node with data that matches the key
        Returns Node if it exists or None if Node doesn't exist
        """
        current_node = self.head
        previous_node = None
        found = False

        while current_node and not found:
            if current_node.data == key and current_node is self.head:
                self.head = current_node.next_node
                found = True
            elif current_node.data == key:
                previous_node.next_node = current_node.next_node
                found = True
            else:
                previous_node = current_node
                current_node = current_node.next_node

        return current_node

    def __repr__(self):
        current_node = self.head
        nodes = []

        while current_node:
            if current_node is self.head:
                nodes.append(f"[Head: {current_node.data}]")
            elif current_node.next_node is None:
                nodes.append(f"[Tail: {current_node.data}]")
            else:
                nodes.append(f"[{current_node.data}]")
            current_node = current_node.next_node

        return "->".join(nodes)
