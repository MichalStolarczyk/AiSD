from binarytree import tree, bst, heap
from typing import Any, Callable, List
from BinaryNode import BinaryNode

class BinaryTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)


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

tree = BinaryTree(10)
assert tree.root.value == 10
tree.root.add_right_child(2)
assert tree.root.right_child.value == 2
tree.root.right_child.add_right_child(1)
assert tree.root.right_child.is_leaf() is False
tree.root.add_left_child(1)
tree.root.left_child.add_left_child(1)
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True
tree.root.left_child.add_right_child(1)
tree.root.right_child.add_left_child(1)
