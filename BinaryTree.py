# A node in a Binary Tree has data, left, and right properties
# The left and right properties are intialized as null
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # the representaion of the data as a string
    def __str__(self):
        return f'{self.data}'

class BinaryTree:
    # When a new Tree is initialized, it has a null root property
    # This means the Tree begins as empty
    def __init__(self):
        self.root = None

    def insert(self, data):
        '''
			Insert(data: any) -> None:\n 
			creates a new Node from the data passed in and adds it to the tree
			If the data is already in the tree, does not insert it again
        '''

        # create new node
        new_node = Node(data)

        # if there is no root node, set new node to root node
        if not self.root:
            self.root = new_node
            return

        # loop over tree starting at the root
        current_node = self.root
        while current_node:
            # if the data is smaller than left
            if data < current_node.data:
                # ...and there is no left
                if not current_node.left:
                    # ...set data to to left node
                    current_node.left = new_node
                    return
                # ...otherwise set current_node to left node
                else:
                    current_node = current_node.left
            # if the data is bigger than the right node
            elif data > current_node.data:
                # ...and there is no right node
                if not current_node.right:
                    # ...the data becomes the right node
                    current_node.right = new_node
                    return
                # ...otherwise move to the right
                else:
                    current_node = current_node.right
            # return if duplicate
            else:
                return

    def search(self, val):
        '''
			search(value: any) -> value or bool:\n 
			Performs depth first search
			Search the Tree for a node with the given value
			If the node exists, return it
			If the node doesn't exist, return false
        '''

        # case where there is not root yet
        if not self.root:
            return False

        # loop through tree starting at the root
        current_node = self.root
        while current_node:
            # if the value is smaller than the
            if val < current_node.data:
                current_node = current_node.left
            elif val > current_node.data:
                current_node = current_node.right
            else:
                return current_node

        return False  # Outside loop means we did not find it!

    # print out all the nodes
    def print(self, node=None):
        '''
			print(node=optional: Node) -> None:\n
			prints out all values recursively (in a breadth first search fashion)
			defualt start is at root node
        '''

        if not node:
            node = self.root

        # first print the current node
        print(node)
        # recursively invoke if another node is found
        if node.left:
            self.print(node.left)
        if node.right:
            self.print(node.right)

    # breadth first search
    # Calculate the number of nodes in the tree, starting from the given node
    # If no node is provided, we can use the root as a sensible default
    def size(self, node=None):
        '''
			size(node=optional: Node) -> int:\n 
			performs breadth first search
			Calculate the number of nodes in the tree, starting from the given node
			If no node is provided, we can use the root as a sensible default
        '''
        # defualt to root
        if not node:
            node = self.root

        count = 0

        def recursive_size(node):
            nonlocal count
            if node:
                count += 1
                recursive_size(node.left)
                recursive_size(node.right)
        recursive_size(node)
        return count

    # Calculate the maximum amount of nodes in any one path from the given node
    # If not given a specific node, default to using the root node
    def height(self, node=None):
        '''
			height(node=optional: Node) -> int:\n 
			perform breadth first search
			Calculate the maximum amount of nodes in any one path from the given node
			If not given a specific node, default to using the root node
        '''

        # defualt to root
        if not node:
            node = self.root

        max_height = 0

        def recursive_height(node, height=1):
            nonlocal max_height
            if node:
                if height > max_height:
                    max_height = height

                recursive_height(node.left, height + 1)
                recursive_height(node.right, height + 1)

        recursive_height(node)
        return max_height

    # Return the maximum data value stored in the tree
    def get_max(self):
        '''
			getMax() -> int:\n 
			perform depth first search
			Calculate the maximum value held in the tree
        '''

        if not self.root:
            return None

        current_node = self.root
        while current_node.right:
            current_node = current_node.right

        return current_node.data

    def get_min(self):
        '''
			getMin() -> int:\n 
			perform depth first search
			Calculate the minimum value held in the tree
        '''

        if not self.root:
            return None

        current_node = self.root
        while current_node.left:
            current_node = current_node.left

        return current_node.data
