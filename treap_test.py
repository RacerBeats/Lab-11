# Ryan Cheung & Francisco Ortega - responsible for this file
# Group Members: Dillan Desai (ID: 10629536) , Ryan Cheung (ID: 10754470), Francisco Ortega (ID: 10758041)
# Course Section: CS 034 - 39575
# Instructor: Prof. Ashraf
# Date: 5/11/25
# Chapter 11 Lab: Heaps and Treaps

from treap import TreapNode, insert, search

def print_treap(node, level=0, prefix="Root: "):
    """Helper function to print the treap structure."""
    if node is not None:
        print(" " * level + prefix + f"[Key: {node.key}, Priority: {node.priority}]")
        if node.left or node.right:
            print_treap(node.left, level + 4, "L--- ")
            print_treap(node.right, level + 4, "R--- ")

def in_order_traversal(node, result=None):
    """Helper function for in-order traversal."""
    if result is None:
        result = []
    if node:
        in_order_traversal(node.left, result)
        result.append(node.key)
        in_order_traversal(node.right, result)
    return result

def test_insert_and_structure():
    print("\n=== Testing Basic Insert and Structure ===")
    root = None
    
    # Insert a few nodes
    root = insert(root, 10, 5)
    root = insert(root, 5, 3)
    root = insert(root, 15, 7)  # This should become the root due to higher priority
    
    print("Treap structure after insertions:")
    print_treap(root)
    
    # Check if the structure is correct
    assert root.key == 15 and root.priority == 7, "Root should be key=15 with priority=7"
    assert root.left.key == 10 and root.left.priority == 5, "Left child should be key=10 with priority=5"
    assert root.left.left.key == 5 and root.left.left.priority == 3, "Left-left child should be key=5 with priority=3"
    
    print("Basic structure test passed!")
    return root

def test_bst_property(root):
    print("\n=== Testing BST Property ===")
    # Get in-order traversal
    result = in_order_traversal(root)
    print(f"In-order traversal: {result}")
    
    # Check if it's sorted
    assert result == sorted(result), "BST property violated: in-order traversal should be sorted"
    print("BST property test passed!")

def test_heap_property(node):
    print("\n=== Testing Heap Property ===")
    if node is None:
        return True
    
    heap_property_valid = True
    
    if node.left:
        if node.priority < node.left.priority:
            print(f"Heap property violated at node {node.key}: parent priority {node.priority} < left child priority {node.left.priority}")
            heap_property_valid = False
        heap_property_valid = heap_property_valid and test_heap_property(node.left)
    
    if node.right:
        if node.priority < node.right.priority:
            print(f"Heap property violated at node {node.key}: parent priority {node.priority} < right child priority {node.right.priority}")
            heap_property_valid = False
        heap_property_valid = heap_property_valid and test_heap_property(node.right)
    
    return heap_property_valid

def test_complex_insertion():
    print("\n=== Testing Complex Insertion Sequence ===")
    root = None
    
    # Insert with priorities that will cause multiple rotations
    insertions = [
        (5, 10), (3, 20), (8, 15), (1, 5), (4, 25), (7, 30), (10, 12)
    ]
    
    print("Inserting nodes (key, priority):", insertions)
    
    for key, priority in insertions:
        root = insert(root, key, priority)
    
    print("\nFinal treap structure:")
    print_treap(root)
    
    # Verify BST property
    test_bst_property(root)
    
    # Verify heap property
    assert test_heap_property(root), "Heap property test failed!"
    print("Heap property test passed!")
    
    return root

def test_search(root):
    print("\n=== Testing Search Functionality ===")
    
    # Test searching for existing keys
    keys_to_find = [1, 4, 7, 10]
    for key in keys_to_find:
        node = search(root, key)
        if node:
            print(f"Found key {key} with priority {node.priority}")
            assert node.key == key, f"Search returned wrong node for key {key}"
        else:
            print(f"Key {key} not found!")
            assert False, f"Search failed to find existing key {key}"
    
    # Test searching for non-existing key
    non_existing_key = 100
    node = search(root, non_existing_key)
    assert node is None, f"Search should return None for non-existing key {non_existing_key}"
    print(f"Correctly returned None for non-existing key {non_existing_key}")
    
    print("Search functionality test passed!")

if __name__ == "__main__":
    print("Starting Treap Tests...")
    
    # Test basic insertion and structure
    simple_root = test_insert_and_structure()
    
    # Test BST property on simple tree
    test_bst_property(simple_root)
    
    # Test heap property on simple tree
    assert test_heap_property(simple_root), "Heap property test failed on simple tree!"
    print("Heap property test passed on simple tree!")
    
    # Test more complex insertion sequence
    complex_root = test_complex_insertion()
    
    # Test search functionality
    test_search(complex_root)
    
    print("\nAll tests passed successfully!")
