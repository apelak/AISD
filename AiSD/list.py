from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value: Any):
        self.value = value
        self.next = None


class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        temp = self.head
        self.head = Node(value)
        self.head.next = temp
        if temp is None:
            self.tail = self.head

    def append(self, value: Any) -> None:
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(value)
        self.tail = temp.next

    def node(self, at: int) -> Node:
        temp = self.head
        for x in range(at):
            temp = temp.next
        return temp

    def insert(self, value: Any, after: Node) -> None:
        new = Node(value)
        new.next = after.next
        after.next = new

    def pop(self) -> Any:
        temp = self.head
        self.head = self.head.next
        return temp

    def remove_last(self) -> Any:
        temp = self.head
        while temp.next.next:
            temp = temp.next
        to_return = temp.next
        self.tail = temp
        temp.next = None
        return to_return

    def remove(self, after: Node) -> None:
        after.next = after.next.next

    def __str__(self) -> str:
        w = ''
        if self.head is None:
            return w
        temp = self.head
        w += f'{temp.value}'
        while temp.next:
            temp = temp.next
            w += f' -> {temp.value}'
        return w

    def __len__(self) -> int:
        it = 0
        temp = self.head
        while temp:
            it += 1
            temp = temp.next
        return it
