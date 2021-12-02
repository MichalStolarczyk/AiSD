from typing import Any
from zad1 import LinkedList


class Queue:
    list: LinkedList

    def __init__(self):
        self.list = LinkedList()

    def __len__(self):
        return self.list.__len__()

    def __str__(self):
        list_items = []
        current_element = self.list.head
        while current_element is not None:
            list_items.insert(0 ,current_element.value)
            current_element = current_element.next
        return ", ".join(list_items)


    def peek(self) -> Any:
        current_element = self.list.head
        while current_element is not None:
            current_element = current_element.next
        return current_element

    def enqueue(self, element: Any) -> None:
        self.list.push(element)

    def dequeue(self) -> Any:
        return self.list.remove_last()

queue = Queue()
assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
print(queue)
assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2