class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class L:
    def __init__(self):
        self.Head = None
        self.Tail = None

    def insert(self, node):
        if self.Head and self.Tail is None:
            self.Head == Node(node)
            self.Tail == Node(node)
        else:
            self._insert(value,cur_node)

    def _insert(self, value, cur_node):
