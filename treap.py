# Ryan Cheung & Francisco Ortega - responsible for this file
# Group Members: Dillan Desai (ID: 10629536) , Ryan Cheung (ID: 10754470), Francisco Ortega (ID: 10758041)
# Course Section: CS 034 - 39575
# Instructor: Prof. Ashraf
# Date: 5/11/25
# Chapter 11 Lab: Heaps and Treaps

class TreapNode:
    key
    priority
    left
    right


    constructor(key, priority):
        set self.key = key
        set self.priority = priority
        set self.left = null
        set self.right = null

function insert(node, key, priority):
    if node is null:
        return new TreapNode(key, priority)

    if key < node.key:
        node.left = insert(node.left, key, priority)
        if node.left.priority > node.priority:
            node = RightRotation(node)

    else if key > node.key:
        node.right = insert(node.right, key, priority)
        if node.right.priority > node.priority:
            node = LeftRotation(node)
    return node

function RightRotation(node):
    leftChild = node.left
    node.left = leftChild.right
    leftChild.right = node
    return leftChild
function LeftRotation(node):
    rightChild = node.right
    node.right = rightChild.left
    rightChild.left = node
    return rightChild
function search(node, key):
    if node is null or node.key == key:
        return node

    if key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)