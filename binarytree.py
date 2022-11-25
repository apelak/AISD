from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = BinaryNode
        self.right_child = BinaryNode

    def is_leaf(self) -> bool:
        if self.left_child and self.right_child:
            return True
        else:
            return False

    def add_left_child(self, value: Any) -> None:
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_in_order(visit())
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit())

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_post_order(visit())
        if self.right_child:
            self.right_child.traverse_post_order(visit())

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit())
        if self.right_child:
            self.right_child.traverse_pre_order(visit())


class BinaryTree:
    root: BinaryNode

    def __init__(self, root):
        self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)



def print_binary_tree(binary_tree: BinaryNode):
    print(binary_tree.value)


