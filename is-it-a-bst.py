import queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = TreeNode(data)
        new_stack = queue.Queue()
        if self.head is None:
            self.head = new_node
            return
        pop = self.head
        while pop:
            if pop.left is None:
                pop.left = new_node
                break
            elif pop.right is None:
                pop.right = new_node
                break
            else:
                new_stack.put(pop.left)
                new_stack.put(pop.right)
            pop = new_stack.get()

    def display(self):
        def _display(node):
            if node:
                _display(node.left)
                print(node.data, end=" ")
                _display(node.right)
        _display(self.head)

    def is_bst(self):
        def _is_bst(node, min_val=None, max_val=None):
            if node is None:
                return True
            if (min_val is not None and node.data <= min_val) or (max_val is not None and node.data >= max_val):
                return False
            return (_is_bst(node.left, min_val, node.data) and _is_bst(node.right, node.data, max_val))

        if _is_bst(self.head):
            print("eh bst")
        else:
            print("nao eh bst")


tree = Tree()
for val in [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]:
    tree.insert(val)

tree.display()
print()
tree.is_bst()