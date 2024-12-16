class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.key)


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        return self._balance(node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        elif key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                return temp
            elif node.right is None:
                temp = node.left
                return temp

            temp = self.get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        if node is None:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        return self._balance(node)

    def update(self, old_key, new_key):
        self.root = self._update(self.root, old_key, new_key)

    def _update(self, node, old_key, new_key):
        node = self.search(node, old_key)
        if node:
            node.key = new_key
            node = self._balance(node)
        return node

    def _balance(self, node):
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate(node, "right")
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate(node.left, "left")
            return self.rotate(node, "right")
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate(node, "left")
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate(node.right, "right")
            return self.rotate(node, "left")

        return node

    def search(self, root, key):
        if not root or root.key == key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def rotate(self, z, direction):
        if direction == "left":
            y = z.right
            T2 = y.left
            y.left = z
            z.right = T2
        elif direction == "right":
            y = z.left
            T3 = y.right
            y.right = z
            z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    @staticmethod
    def get_height(node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def draw_tree(self):
        self._draw_tree(self.root)

    def _draw_tree(self, node, prefix="", is_left=True):
        if node is not None:
            self._draw_tree(node.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(node.key))
            self._draw_tree(node.left, prefix + ("    " if is_left else "│   "), True)


avl = AVLTree()

arrs = [10, 20, 30, 40, 50, 25]

for k in arrs:
    avl.insert(k)
    print(avl.root)

avl.update(30, 35)
avl.insert(15)
avl.insert(16)
avl.insert(17)
avl.insert(26)
avl.draw_tree()
