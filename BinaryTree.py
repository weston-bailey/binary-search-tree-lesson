class Node:
    def __init__(self, data):
        # value at current node
        self.data = data 
        # larger value node
        self.right = None
        # smaller value node
        self.left = None
    
    def __str__(self):
        return f'{self.data}'


# node tester area
# root = Node(15)
# root.left = Node(10)
# root.right = Node(21)

# print(f'root: {root}, left: {root.left}, right: {root.right}')

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        '''
            Insert(data: any) -> None:\n 
            creates a new Node from the data passed in and adds it to the tree
            If the data is already in the tree, does not insert it again
        '''
        # create a new node
        new_node = Node(data)
        # if there is no root, set new node to be root
        if not self.root:
            self.root = new_node
            return

        # iterate the tree and find where to insert the new node
        # start iteration at the root node
        current_node = self.root
        while current_node:
            # if the new node's data is greater than the current node
            if new_node.data > current_node.data:
                # insert to the right if no value is found
                if not current_node.right:
                    current_node.right = new_node
                    return
                # value has been found -- we keep iterating
                else:
                    current_node = current_node.right
            # if the new node's data is less than the current node
            elif new_node.data < current_node.data:
                # if no left exists -- insert here
                if not current_node.left:
                    current_node.left = new_node
                    return
                # if left exists -- keep iterating
                else:
                    current_node = current_node.left
            # if they are equal -- just return (no duplicates)
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
        # if there is no root, immediately return false
        if not self.root:
            return False

        # start at the root of the tree
        current_node = self.root
        while current_node:
            # if the value is smaller than the current data -- move left
            if val < current_node.data:
                current_node = current_node.left
            # if the value is greater than the current data - move right
            elif val > current_node.data:
                current_node = current_node.right
            # if the value is equal to the current data -- return the current_node!
            else:
                return current_node
        
        # if we make it out of the loop, we need to return false
        return False


    def bfs(self, val):
        '''
            bfs(val: any) -> value or bool:\n
            Performs breadth first search
            Search the Tree for a node with the given value
            If the node exists, return it
            If the node doesn't exist, return false
        '''
        
        # if there is no root, return false immediately
        if not self.root:
            return False

        # queue to keep track of each level as we travers
        queue = [self.root]

        while len(queue) > 0:
            # pop off the first item in the queue and examine it
            current_node = queue.pop(0)
            # print(f'currently checking: {current_node}')
            # if current node has the value we are looking for, return the current
            if current_node.data == val:
                return current_node
            
            # check if the current node has children, and toss them in the queue for future processing 
            if current_node.left is not None:
                queue.append(current_node.left)
            
            if current_node.right is not None:
                queue.append(current_node.right)
            
        # if the loop ends, the queue is empty and we did not find val
        return False
    
    # print out all the nodes
    def print(self, node=None):
        '''
            print() -> None:\n
            prints out all values recursively (in a depth first search fashion)
            default start is at root node
        '''
        # if no node has been provided as an arg, start at root
        if not node:
            node = self.root
        
        # this gives us inorder traversal
        # prints out lower vals first
        # print(node)

        # if another node is found, recursive invoke
        if node.left:
            self.print(node.left)
        
        # # print the current node
        # this gives us inorder traversal
        print(node)

        if node.right:
            self.print(node.right)

        # prints the tree up from the bottom
        # print(node)


tree = BinaryTree()
# test root insertion
tree.insert(15)
# test left side insertion
tree.insert(10)
# test right side insertion
tree.insert(21)
tree.insert(14)
tree.insert(3)
tree.insert(1)
tree.insert(4)
tree.insert(12)
tree.insert(14)

tree.insert(17)
tree.insert(24)
tree.insert(16)
tree.insert(19)
# tree.print()
# print(tree.dfs(23))
print(tree.bfs(100))
