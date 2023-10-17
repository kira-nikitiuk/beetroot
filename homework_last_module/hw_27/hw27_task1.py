class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end=' ')
        inorder(root.right)

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

def insertTree(root, tree_to_insert):
    if tree_to_insert is not None:
        root = insertTree(root, tree_to_insert)
    return root

def deleteSubtree(root, key_to_delete):
    if root is None:
        return root
    if root.key == key_to_delete:
        return None
    root.left = deleteSubtree(root.left, key_to_delete)
    root.right = deleteSubtree(root.right, key_to_delete)
    return root

root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

new_tree = None
new_tree = insert(new_tree, 2)
new_tree = insert(new_tree, 1)
new_tree = insert(new_tree, 3)

root = insertTree(root, new_tree)
print("\nInorder traversal after inserting a tree: ", end=' ')
inorder(root)

root = deleteSubtree(root, 3)
print("\nInorder traversal after deleting a subtree: ", end=' ')
inorder(root)
