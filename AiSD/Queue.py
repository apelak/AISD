from typing import Any
from list import LinkedList


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def peek(self) -> Any:
        return self._storage.head.data

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        self._storage.pop()


queue = Queue()
queue.enqueue(1)
queue.peek()
queue.dequeue()
