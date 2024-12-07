class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key) + " { " + str(self.left) +" "+ str(self.right) + " } "


class Tree:
    def __init__(self, root: Node = None):
        self.root = root

    def add(self, key):
        self.root = self._add(self.root, key)

    def _add(self, node, key):
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self._add(node.left, key)
        else:
            node.right = self._add(node.right, key)
        return node

    def _reverse(self,node):
        if not node:
            return node
        node.left, node.right = node.right, node.left
        self._reverse(node.left)
        self._reverse(node.right)
        return node

    def reverse(self):
        self.root = self._reverse(self.root)

    def __str__(self):
        return str(self.root)


root = Node(10)
tree = Tree(root)

tree.add(5)
tree.add(7)

print(tree)
