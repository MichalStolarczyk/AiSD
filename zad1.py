from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    head: 'Node'

    def __init__(self):
        self.head = None

    def __len__(self):
        index = 0
        current_element = self.head
        while current_element is not None:
            index += 1
            current_element = current_element.next
        return index

    def __str__(self):
        list_items = ''
        current_element = self.head
        while current_element is not None:
            if current_element.next is None:
                list_items += f'{current_element.value}'
            else:
                list_items += f'{current_element.value} -> '
            current_element = current_element.next
        return list_items

    def append(self, value: Any) -> None:
        element = Node(value)
        if self.head is None:
            self.head = element
        else:
            current_element = self.head
            while current_element.next is not None:
                current_element = current_element.next
            current_element.next = element

    def push(self, value: Any) -> None:
        element = Node(value)
        element.next = self.head
        self.head = element

    def node(self, at: int):
        index = 0
        current_element = self.head
        while current_element is not None:
            if index == at:
                return current_element
            current_element = current_element.next
            index += 1

    def insert(self, value: Any, after: Node):
        element = Node(value)
        current_element = self.head
        for x in range(after):
            current_element = current_element.next
        current_element_next = current_element.next
        element.next = current_element_next
        current_element.next = element

    def pop(self):
        current_head = self.head
        new_head = self.head.next
        self.head = new_head
        return current_head

    def remove_last(self):
        current_element = self.head
        while current_element.next.next is not None:
            current_element = current_element.next
        last = current_element.next.value
        current_element.next = None
        return last



#list = LinkedList()
#list.append(1)
#print(list)
#list.append(2)
#print(list)
#list.push(3)
#print(list)
#list.push(4)
#print(list)
#first_element = list.node(0)
#print(list)
#list.insert(8, 2)
#print(list)
#list.pop()
#print(list)
#list.remove_last()
#print(list)
#print(len(list))
