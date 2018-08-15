class Node(object):
    def __init__(self, key):
        self.next = None
        self.value = key


    # Insert Node
    def insert(self, value):
        if not self.value:
            self.value = value
        else:
            self.next = Node(value)

    def print_list(self, root):
        res = []
        if root:
            res.append(root.value)
            self.print_list(root.next)
        return res

root = Node(19)
root.insert(2)
root.insert(24)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(1)
root.insert(31)
root.insert(42)

print(root.print_list(root))