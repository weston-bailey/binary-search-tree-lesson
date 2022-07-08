from threading import currentThread


class Node:
    # here we will add the constructor
    # creating new node
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data 
    
    # and the string method
    # need along with __init__
    def __str__(self):
        return f'{self.data}'


class BinaryTree:
    # the tree will start out empty, with a null head
    # root is = head
    def __init__(self):
        self.root = None

    def insert(self, data):
        '''
        Insert(data: any) -> None:\n 
        creates a new Node from the data passed in and adds it to the tree
        If the data is already in the tree, does not insert it again
        '''
        # Create new node from the data passed in
        new_node = Node(data)
        # If the root doesn't exist, set the new node to be the root
        if not self.root:
            self.root = new_node
            return
        # loop over the tree starting at the root
        current_node = self.root
        while current_node:
            # If data is SMALLER than the Left
            if data < current_node.data:
                # ...and there is no left node
                if not current_node.left:
                    #set the data to be the let node
                    current_node.left = new_node
                    return
                # ...otherwise set current_node to the left (one already exists)
                else:
                    current_node = current_node.left

            # If data is BIGGER that Left
            elif data > current_node.data:
                #...and there is not a right node
                if not current_node.right:
                    # insert new node to the right
                    current_node.right = new_node
                    return
                #otherwise, a right exists, so the right becomes the current node
                else:
                    current_node = current_node.right
            
            # the data is DUPLICATE
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
        # if there is no root - return False
        if not self.root:
            return False
        # if root exists. Loop through the tree, starting at the root
        current_node = self.root
        while current_node:
            # if the value is smaller than the current node's data
            if val < current_node.data:
                current_node = current_node.left
            elif val > current_node.data:
                #move to the right
                current_node = current_node.right
            else:
                # this means that they are equal
                return current_node

        #return False -- not found
        return False
            
    def print(self, node=None):
        '''
        print(node=optional: Node) -> None:\n
        prints out all values recursively (in a depth first search fashion)
        defualt start is at root node
        '''
        if not node:
            node = self.root

        #print the node
        print(node)
        #if there is a left, recusively invoke
        if node.left:
            self.print(node.left)

        if node.right:
            self.print(node.right)

    def size(self, node=None):
        '''
        size(node=optional: Node) -> int:\n 
        performs breadth first search
        Calculate the number of nodes in the tree, starting from the given node
        If no node is provided, we can use the root as a sensible default
        '''
     # if no node is passed in, default using root
        if not node:
            node = self.root
        
        count = 0

        def recursive_count(node):
            nonlocal count
            #if node is None, increase count and recurse on the left and right
            if node:
                count += 1
                recursive_count(node.left)
                recursive_count(node.right)
        
        recursive_count(node)
        return count


    def height(self, node=None):
        '''
        height(node=optional: Node) -> int:\n 
        perform breadth first search
        Calculate the maximum amount of nodes in any one path from the given node
        If not given a specific node, default to using the root node
        '''
        # # if not self.root:
        # #         return 0

        # if not node:
        #         node = self.root

        # left_height = level
        # right_height = level
        # if node.left:
        #         left_height = self.height(node.left, level + 1)
        # if node.right:
        #         right_height = self.height(node.right, level + 1)

        # return max(left_height, right_height)

        ##ALTERNATE SOLUTION
        if not node:
            node = self.root

            max_height = 0

        def recurse_height(node, height):
            nonlocal max_height
            if node:
                if height > max_height:
                    max_height = height

            recurse_height(node.left, height + 1)
            recurse_height(node.right, height + 1)

            recurse_height(node, 1)
            return max_height


    def get_max(self):
        '''
        getMax() -> int:\n 
        perform depth first search
        Calculate the maximum value held in the tree
        '''
        if not self.root:
            return False
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
            return False
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node.data
