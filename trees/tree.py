import collections

class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


# Insert Node
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

# In Order
    def in_order(self, root):
        res = []
        if root:
            res = self.in_order(root.left)
            res.append(root.value)
            res += self.in_order(root.right)
        return res

# Post Order
    def p_order(self, root):
        res = []
        if root:
            res = self.p_order(root.left)
            res += self.p_order(root.right)
            res.append(root.value)
        return res

# Pre Order
    def pre_order(self, root):
        res = []
        if root:
            res.append(root.value)
            res += self.pre_order(root.left)
            res += self.pre_order(root.right)
        return res

# Depth
    def levels(self, root):
        if root:
            return 1 + max(self.levels(root.left),self.levels(root.right))
        else:
            return 0

# Balance
    def is_balanced(self, root):
        if root is None:
            return True
        else:
            return self.is_balanced(root.left) and self.is_balanced(root.right)\
                   and abs(self.levels(root.left) - self.levels(root.right)) < 2

# Diameter
    def diameter(self, root):
        if not root:
            return 0
        else:
            return max((1 + self.levels(root.left) + self.levels(root.right)),
                       self.diameter(root.left), self.diameter(root.right))

# Sum
    def sum(self, root):
        if not root:
            return 0
        else:
            return self.value + self.sum(root.left) + self.sum(root.right)

# Count Nodes
    def count_nodes(self, root):
        if not root:
            return 0
        else:
            return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

# Average
    def average(self, root):
        if not root:
            return None
        else:
            return self.sum(root) / self.count_nodes(root)


# Find Node bfs
    def bfs(self, root, value):
        path = ()
        queue = collections.deque([root])
        while queue:
            vertex = queue.popleft()
            for neighbour in root[vertex]:
                if neighbour not in path:
                    path.add(neighbour)
                    queue.append(neighbour)
        return path




root = Node(19)
root.insert(2)
root.insert(24)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(1)
root.insert(31)
root.insert(42)
root.insert(23)
root.insert(43)
root.insert(15)
root.insert(17)
root.insert(18)
# root.insert(43)
# root.insert(44)
# root.insert(45)
# root.insert(46)
# root.insert(47)
# root.insert(48)

print('In Order: ')
print(root.in_order(root))
print('Post Order: ')
print(root.p_order(root))
print('Pre Order: ')
print(root.pre_order(root))
print('Levels: ')
print(root.levels(root))
print("Is Balanced:")
print(root.is_balanced(root))
print("Diameter:")
print(root.diameter(root))
print("Sum:")
print(root.sum(root))
print("Count of Nodes:")
print(root.count_nodes(root))
print("Average:")
print(root.average(root))

# print("BFS: ")
# print(root.bfs(root,3))