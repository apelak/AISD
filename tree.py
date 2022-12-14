from typing import Any, List, Callable, Union
# from graphviz import *


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value) -> None:
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        if self.children:
            return False
        return True

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for i in self.children:
            i.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        q = [self]
        while q:
            visit(q[0])
            for i in q[0].children:
                q.append(i)
            q.pop(0)

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        for i in self.children:
            if i.search(value):
                return i.search(value)

    # def show(self, g=Graph('g')):
    #     g.node(str(self), str(self.value))
    #     for i in self.children:
    #         g.edge(str(self), str(i))
    #         i.show(g)
    #     return g


class Tree:
    root: TreeNode

    def __init__(self, root) -> None:
        self.root = root

    def add(self, value: Any, parent_name: Any) -> None:
        parent_name.children.append(TreeNode(value))

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    # def show(self) -> None:
    #     self.root.show().render(filename='tree', format='png', cleanup=True, view=True)


def print_node(tree: 'TreeNode') -> None:
    if isinstance(tree, TreeNode):
        print(tree.value)
    else:
        print(tree)
        