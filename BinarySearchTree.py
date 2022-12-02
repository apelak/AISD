from typing import Any


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any):
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self) -> 'BinaryNode':
        if self.left_child:
            return self.min(self.left_child)


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root):
        self.root = root

    def insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node is None:
            return node(value)
        else:
            if node.value == value:
                return self.root
            elif node.value < value:
                node.right_child = self.insert(node.right_child, value)
            else:
                node.left_child = self.insert(node.left_child, value)


tree = BinarySearchTree(8)
tree.insert(tree,3)
tree.insert(10)
tree.insert(14)
tree.insert(13)
tree.insert(1)
tree.insert(6)
tree.insert(4)
tree.insert(7)
