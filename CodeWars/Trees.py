import random


class Node:

    def __init__(self, value = None):
        self.value = value
        self.parent = None
        self.LChild = None
        self.RChild = None


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.LChild==None:
                cur_node.LChild=Node(value)
            else:
                self._insert(value, cur_node.LChild)
        elif value > cur_node.value:
            if cur_node.RChild == None:
                cur_node.RChild=Node(value)
            else:
                self._insert(value,cur_node.RChild)
        else:
            print("Value already in tree")

    def count_nodes(self, cur_node):
        if cur_node is not None:
            return 1 + self.count_nodes(cur_node.LChild) + self.count_nodes(cur_node.RChild)
        else:
            return 0

    def levels(self,cur_node):
        if cur_node is None:
            return 0
        else:
            return 1 + max(self.levels(cur_node.LChild), self.levels(cur_node.RChild))

    def is_balanced(self, cur_node):
        if cur_node is None:
            return True
        else:
            if abs(self.levels(cur_node.LChild) - self.levels(cur_node.RChild) > 1):
                return False
            else:
                return self.is_balanced(cur_node.LChild) and self.is_balanced(cur_node.RChild)

    def sum(self, cur_node):
        if cur_node is None:
            return 0
        else:
            return cur_node.value + self.sum(cur_node.LChild) + self.sum(cur_node.RChild)

    def average(self,cur_node):
        return self.sum(cur_node) / self.count_nodes(cur_node)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.LChild)
            print(str(cur_node.value))
            self._print_tree(cur_node.RChild)

    def fill_tree(tree,max =100, rand = 1000):
        for i in range(max):
            tree.insert(random.randint(0,rand))

    def diameter(self, node):
        if node is None:
            return 0
        else:
            return max((self.levels(node.LChild) + self.levels(node.RChild) + 1), self.diameter(node.LChild),self.diameter(node.RChild))

    def pos_order(self, node):
        if node is None:
            return node
        else:
            self.pos_order(node.LChild)
            self.pos_order(node.RChild)
            a.append(node.value)

    def top2bottom(self, node):
        if node is None:
            return node
        else:
            self.top2bottom(node.LChild)
            print(node.value)
            self.top2bottom(node.RChild)

    def find_path(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return [node.value]
        leftPath = self.find_path(node.LChild, value)
        if leftPath is not None:
            leftPath.insert(0,node.value)
            return leftPath
        rightPath = self.find_path(node.RChild, value)
        if rightPath is not None:
            rightPath.insert(0,node.value)
            return rightPath
        return None


    def LCA(self,node,value1, value2):
        ancestors = []
        path1 = self.find_path(node,value1)
        path2 = self.find_path(node,value2)
        # print(path1)
        # print(path2)
        if node is None:
            return node

        while len(path1) > 0 and path1[0] == path2[0]:
            ancestors.append(path1[0])
            path1.pop(0)
            path2.pop(0)
        return ancestors[-1]

    def pre_order(self, node):
        if node is None:
            return node
        else:
            print(node.value)
            self.pre_order(node.LChild)
            self.pre_order(node.RChild)


    def zigzag(self, node):
        toggle = True
        if node is None:
            return node
        print(node.value)
        if toggle:
            print(node.LChild.value)
        else:
            print(node.RChild.value)
            toggle = True

a = []
# tree = Tree()
# tree.insert(6)
# tree.insert(4)
# tree.insert(12)
# tree.insert(3)
# tree.insert(5)
# tree.insert(11)
# tree.insert(15)
# tree.insert(1)
# tree.insert(17)

tree = Tree()
tree.insert(8)
tree.insert(6)
tree.insert(10)
tree.insert(5)
#tree.insert(3)
tree.insert(7)
tree.insert(9)
tree.insert(11)

print(tree.root.value)
print(tree.root.LChild.value)
print(tree.root.RChild.value)
print(tree.root.LChild.LChild.value)
print(tree.root.LChild.RChild.value)
print(tree.root.RChild.LChild.value)
print(tree.root.RChild.RChild.value)



print("The nodes in the Tree are: ", tree.count_nodes(tree.root))
print("Height of Tree: ",tree.levels(tree.root))
print("The Tree is balanced: ", tree.is_balanced(tree.root))
print("The sum of values is: ", tree.sum(tree.root))
print("The average of values is: ", tree.average(tree.root))
print("Diameter of the tree is: ", tree.diameter(tree.root))

b = [5, 7, 6, 9, 11, 10, 8]
print("Is this list a post order run of the tree: {} ? ".format(b))

tree.pos_order(tree.root)
print(a)

if a == b: print("True")
else: print("False")

tree.top2bottom(tree.root)

print(tree.find_path(tree.root, 11))

print(tree.LCA(tree.root,9,7))

tree.pre_order(tree.root)

tree.zigzag(tree.root)