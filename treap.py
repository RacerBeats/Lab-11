# Ryan Cheung & Francisco Ortega - responsible for this file
# Group Members: Dillan Desai (ID: 10629536) , Ryan Cheung (ID: 10754470), Francisco Ortega (ID: 10758041)
# Course Section: CS 034 - 39575
# Instructor: Prof. Ashraf
# Date: 5/11/25
# Chapter 11 Lab: Heaps and Treaps

class TreapNode:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

def insert(node, key, priority):
    if node is None:
        return TreapNode(key, priority)

    if key < node.key:
        node.left = insert(node.left, key, priority)
        if node.left.priority > node.priority:
            node = right_rotation(node)

    elif key > node.key:
        node.right = insert(node.right, key, priority)
        if node.right.priority > node.priority:
            node = left_rotation(node)
    return node

def right_rotation(node):
    left_child = node.left
    node.left = left_child.right
    left_child.right = node
    return left_child

def left_rotation(node):
    right_child = node.right
    node.right = right_child.left
    right_child.left = node
    return right_child

def search(node, key):
    if node is None or node.key == key:
        return node

    if key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)
