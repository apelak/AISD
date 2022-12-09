

from typing import Any, List


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
        return self

    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root):
        self.root = root

    def insert(self, value: Any) -> None:
        if self.contains(value):
            return
        self.root = self.__insert(self.root, value)

    def __insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node:
            if value < node.value:
                node.left_child = self.__insert(node.left_child, value)
            else:
                node.right_child = self.__insert(node.right_child, value)
        else:
            node = BinaryNode(value)
        return node

    def insert_list(self, list_: List[Any]) -> None:
        for i in list_:
            self.insert(i)

    def contains(self, value: Any) -> bool:
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            if temp.value < value:
                return self.contains(temp.left_child, value)
            else:
                return self.contains(temp.right_child, value)
        return False

    def remove(self, value: Any) -> None:
        if self.contains(value):
            self.root = self.__remove(self.root, value)
        else:
            return

    def __remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value == node.value:
            if node.right_child and node.left_child:
                node.value = node.right_child.min().value
                node.right_child = self.__remove(node.right_child, node.right_child.min().value)
            elif node.right_child:
                node = node.right_child
            elif node.left_child:
                node = node.left_child

            else:
                if node == self.root:
                    node.value = 0
                else:
                    node = None
        elif value > node.value:
            node.right_child = self.__remove(node.right_child, value)
        else:
            node.left_child = self.__remove(node.left_child, value)
        return node



