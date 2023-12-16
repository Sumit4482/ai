# max utility of binary tree using minmax algorithm

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_value(node):
    if node.left is None and node.right is None:
        return node.data
    return max(min_value(node.left), min_value(node.right))


def min_value(node):
    if node.left is None and node.right is None:
        return node.data
    return min(max_value(node.left), max_value(node.right))


def main():
    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Max Utility of Binary Tree using MinMax Algorithm: ", max_value(root))

main()
