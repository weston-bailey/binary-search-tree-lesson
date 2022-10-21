class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # the representation of the data as a string
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
    
    def dfs(self, val):
        '''
            dfs(val: any) -> value or bool:\n 
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

    def bfs(self, val):
        '''
            bfs(val: any) -> value or bool:\n
            Performs bredth first search
            Search the Tree for a node with the given value
            If the node exists, return it
            If the node doesn't exist, return false
        '''
        if self.root is None:
            return False

        queue = [self.root]


        while len(queue) > 0:
            cur_node = queue.pop(0)
            
            if cur_node.data == val:
                return cur_node

            if cur_node.left is not None:
                queue.append(cur_node.left)

            if cur_node.right is not None:
                queue.append(cur_node.right)
        
        return False

    # print out all the nodes
    def print(self, node=None):
        '''
            print() -> None:\n
            prints out all values recursively (in a depth first search fashion)
            default start is at root node
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

    # ## # ## # ## # ## #
    # Challenges

    def size(self):
        '''
            size() -> int:\n 
            Calculate the number of nodes in the tree, starting from the root
        '''
        count = 0

        def recursive_size(node):
            nonlocal count
            if node:
                count += 1
                recursive_size(node.left)
                recursive_size(node.right)

        recursive_size(self.root)

        return count

    def height(self):
        '''
            height() -> int:\n 
            Calculate the maximum depth of nodes starting at the root
        '''

        max_height = 0

        def recursive_height(node, height=1):
            nonlocal max_height
            if node:
                if height > max_height:
                    max_height = height

                recursive_height(node.left, height + 1)
                recursive_height(node.right, height + 1)

        recursive_height(self.root)
        return max_height

    # Return the maximum data value stored in the tree
    def get_max(self):
        '''
            get_max() -> int:\n 
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
            get_min() -> int:\n 
            perform depth first search
            Calculate the minimum value held in the tree
        '''

        if not self.root:
            return None

        current_node = self.root
        while current_node.left:
            current_node = current_node.left

        return current_node.data

    def inorder_traversal(self):
        # https://leetcode.com/problems/binary-tree-inorder-traversal/
        order = []

        def traverse(node):
            nonlocal order
            if not node:
                return None

            traverse(node.left)

            order.append(node.data)

            traverse(node.right)
        
        traverse(self.root)

        return order
    
    def level_order(self):
        # https://leetcode.com/problems/binary-tree-level-order-traversal/
        if not self.root:
            return []

        queue = [self.root]
        out = []

        while len(queue):
            level = []
            level_len = len(queue)
            for _ in range(level_len):
                current_node = queue.pop()
                level.append(current_node.data)

                if current_node.left:
                    queue.insert(0, current_node.left)
                if current_node.right:
                    queue.insert(0, current_node.right)


            out.append(level)

        return out

    def is_valid(self):
        # https://leetcode.com/problems/validate-binary-search-tree/
        order = self.inorder_traversal()

        for i in range(1, len(order)):
            if order[i] <= order[i - 1]:
                print(order[i], order[i - 1])
                return False

        return True