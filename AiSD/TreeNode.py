from typing import Any, List, Callable
from Queue import Queue


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value: Any):
        self.value: Any = value
        self.children: List = []

    def is_leaf(self) -> bool:
        if self.children:
            return False
        return True

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for x in self.children:
            x.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        queue = Queue()
        queue.enqueue(self)
        while queue:
            temp = queue.peek()
            visit(queue.peek())
            queue.dequeue()
            for x in temp.children:
                queue.enqueue(x)


    # def search(self, value: Any) -> Any:



t = print


def print(adres: 'TreeNode') -> None:
    if isinstance(adres, TreeNode):
        t(adres.value)
    else:
        t(adres)
