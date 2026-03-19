class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class Tree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def add(self, parent_node, new_value):
        new_node = Node(new_value)
        parent_node.add_child(new_node)
        return new_node

    def print_tree(self):
        self._print_tree(self.root, "", True)

    def _print_tree(self, node, prefix, is_last):
        if node is not None:
            print(prefix + ("└── " if is_last else "├── ") + str(node.value))

            prefix += "    " if is_last else "│   "

            for i, child in enumerate(node.children):
                is_last_child = (i == len(node.children) - 1)
                self._print_tree(child, prefix, is_last_child)

    def is_balanced(self):
        return self._check_balance(self.root) != -1

    def _check_balance(self, node):
        if node is None:
            return 0

        heights = []

        for child in node.children:
            h = self._check_balance(child)
            if h == -1:
                return -1
            heights.append(h)

        if not heights:
            return 1

        if max(heights) - min(heights) > 1:
            return -1

        return max(heights) + 1


tree = Tree("A")

b = tree.add(tree.root, "B")
c = tree.add(tree.root, "C")

d = tree.add(b, "D")
e = tree.add(b, "E")

tree.print_tree()

print("Balanceada?", tree.is_balanced())