class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, value):
        self.root = Node(value)
        self.count = 1


    def size(self):
        print(self.count)  # returns the number of items in tree


    def insert(self, value):
        self.count += 1

        new_node = Node(value)

        def search_tree(node):
            # if value <  node.value, go left
            if value < node.value:
                # if left child doesn't exist, append new node
                if node.left is None:
                    node.left = new_node
                # if left child exist, recursively look left again
                else:
                    search_tree(node.left)

            # value > node.value, go right
            if value >= node.value:
                # if right child doesn't exist, append new node
                if node.right is None:
                    node.right = new_node
                else:
                    search_tree(node.right)

        # invoke recursive function
        search_tree(self.root)


    def contains(self, value):
        current_node = self.root

        while current_node:
            # if value is found return true
            if value == current_node.value:
                print(f"contains {value}: {True}")
                return True

            # if value < current node value, look left
            if value < current_node.value:
                current_node = current_node.left

            # else, look right
            else:
                current_node = current_node.right

        # if value not found return false
        print(f"contains {value}: {False}")
        return False
