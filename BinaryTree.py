from binarytree import tree, bst, heap
from typing import Any, Callable, List
from BinaryNode import BinaryNode

class BinaryTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)

    def __str__(self):
        current = self.root
        str = ""
        str.append(current.value), str.append('\n')
        def printTree(self):
            if current.left_child is not None:
                str.append(current.left_child.value)
            str.append('  ')
            if current.right_child is not None:
                str.append(current.right_child.value)
            str.append('\n')
            printTree(current)


def left_line(tree: BinaryTree) -> List[BinaryNode]:
    list = []
    list.append(tree.root.value)
    currentNode = tree.root
    while currentNode.left_child is not None:
        list.append(currentNode.left_child.value)
        currentNode = currentNode.left_child
    return list

drzewo = BinaryTree(1)
drzewo.root.add_left_child(2)
drzewo.root.add_right_child(9)
drzewo.root.left_child.add_left_child(3)
drzewo.root.left_child.add_right_child(8)
drzewo.root.left_child.left_child.add_left_child(4)
print(left_line(drzewo))