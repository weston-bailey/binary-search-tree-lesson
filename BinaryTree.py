class Node:
    # here we will add the constructor
    def __init__(self, data):
        pass
    # and the string method

    def __str__(self):
        pass


class BinaryTree:
    # the tree will start out empty, with a null head
    def __init__(self):
        pass

    def insert(self, data):
        '''
          Insert(data: any) -> None:\n 
          creates a new Node from the data passed in and adds it to the tree
          If the data is already in the tree, does not insert it again
        '''
        pass

    def search(self, val):
        '''
          search(value: any) -> value or bool:\n 
          Performs depth first search
          Search the Tree for a node with the given value
          If the node exists, return it
          If the node doesn't exist, return false
        '''
        pass

    def print(self, node=None):
        '''
          print(node=optional: Node) -> None:\n
          prints out all values recursively (in a depth first search fashion)
          defualt start is at root node
        '''
        pass

    def size(self, node=None):
        '''
          size(node=optional: Node) -> int:\n 
          performs breadth first search
          Calculate the number of nodes in the tree, starting from the given node
          If no node is provided, we can use the root as a sensible default
        '''
        pass

    def height(self, node=None):
        '''
          height(node=optional: Node) -> int:\n 
          perform breadth first search
          Calculate the maximum amount of nodes in any one path from the given node
          If not given a specific node, default to using the root node
        '''
        pass

    def get_max(self):
        '''
          getMax() -> int:\n 
          perform depth first search
          Calculate the maximum value held in the tree
        '''
        pass

    def get_min(self):
        '''
          getMin() -> int:\n 
          perform depth first search
          Calculate the minimum value held in the tree
        '''
        pass
