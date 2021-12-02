from typing import Any
from zad1 import LinkedList

class Stack:
    list: LinkedList

    def __init__(self):
        self.list = LinkedList()

    def __len__(self):
        return self.list.__len__()

    def __str__(self):
        list_items = 'List:\n'
        current_element = self.list.head
        while current_element is not None:
            if current_element.next is None:
                list_items += f'{current_element.value}\n-------'
            else:
                list_items += f'{current_element.value}\n'
            current_element = current_element.next
        return list_items

    def push(self, element: Any) -> None:
        self.list.append(element)

    def pop(self) -> Any:
        return self.list.remove_last()



stack = Stack()
assert len(stack) == 0
stack.push(3)
stack.push(10)
stack.push(1)
print(stack)

assert len(stack) == 3
print(len(stack))
top_value = stack.pop()
print(top_value)
print(stack)
assert top_value == 1
assert len(stack) == 2
print(len(stack))