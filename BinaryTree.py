from locale import currency


class Node:
  # here we will add the constructor
  def __init__(self, data):
    self.left = None 
    self.right = None
    self.data = data

  # and the string method
  def __str__(self):
    return f'{self.data}'


class BinaryTree:
  # the tree will start out empty, with a null head
  def __init__(self):
    self.root = None

  def insert(self, data):
    '''
      Insert(data: any) -> None:\n 
      creates a new Node from the data passed in and adds it to the tree
      If the data is already in the tree, does not insert it again
    '''

    # create a new node from the data that is pasased in
    new_node = Node(data)

    # if there is not root, the new node becomes the root
    if not self.root:
      self.root = new_node
      return

    # loop over the tree starting at the root
    # keep track of the current node that is being evaluated
    current_node = self.root
    while current_node:
      # if the new node's data is smaller than current
      if new_node.data < current_node.data:
        # ...and there is not left
        if not current_node.left:
          # set the new node to be the left!
          current_node.left = new_node
          return
        # ...otherwise there is a left and we need to reset the current to this left
        else:
          current_node = current_node.left
      # if the new node's data is greater than current
      elif new_node.data > current_node.data:
        # ...and there is no right
        if not current_node.right:
          # set the new node to be the right and return
          current_node.right = new_node
          return
        # ...otherwise we found a right and need to set it to the current and redo the loop
        else:
          current_node = current_node.right

  def search(self, val):
    '''
      search(value: any) -> value or bool:\n 
      Performs depth first search
      Search the Tree for a node with the given value
      If the node exists, return it
      If the node doesn't exist, return false
    '''
    
    # if there is not root -- return false
    if not self.root:
      return False

    # loop through the tree starting at the root
    # keep track of the current node
    current_node = self.root
    while current_node:
      # the value we are searching is is less than the current
      if val < current_node.data:
        current_node = current_node.left
      # greater than the current
      elif val > current_node.data:
        current_node = current_node.right
      # equal to the current -- is a match
      else:
        return current_node

    return False


  def print(self, node=None):
    '''
      print(node=optional: Node) -> None:\n
      prints out all values recursively (in a depth first search fashion)
      defualt start is at root node
    '''
    # if there is no node, set node to be self.root
    if not node:
      node = self.root

    # print the current node
    print(node)
    # if there is a right, invoke print on it
    if node.right: self.print(node.right)
    # if there is a left, invoke print on it
    if node.left: self.print(node.left)

  def size(self, node=None):
    '''
      size(node=optional: Node) -> int:\n 
      performs breadth first search
      Calculate the number of nodes in the tree, starting from the given node
      If no node is provided, we can use the root as a sensible default
    '''
    # if no node is provided, start at root
    if not node:
      node = self.root

    # keep track of a count of nodes
    count = 0
    # recursively loop the tree, coutning nodes
    def recurse_size(node):
      nonlocal count
      if node:
        print(node.data)
        # inc the count is the node exists
        count += 1
        # if node exists invoke sef on left and right
        recurse_size(node.left)
        recurse_size(node.right)
    
    recurse_size(node)
    # return the count
    return count   

  def height(self, node=None):
    '''
      height(node=optional: Node) -> int:\n 
      perform breadth first search
      Calculate the maximum amount of nodes in any one path from the given node
      If not given a specific node, default to using the root node
    '''
    # default to the root node
    if not node:
      node = self.root
    
    # keep track of the max height encountered
    max_height = 0
    # recursive function that keeps track of the height
    def recurse_height(node, height=1):
      # and compares it to the max height
      nonlocal max_height
      # this is also base case
      if node:
        if height > max_height:
          max_height = height
        # inovkes itself on the left and right nodes
        recurse_height(node.left, height + 1)
        recurse_height(node.right, height + 1)
    
    recurse_height(node)
    return max_height

  def get_max(self):
    '''
      getMax() -> int:\n 
      perform depth first search
      Calculate the maximum value held in the tree
    '''
     # if there is not root, then return None
    if not self.root:
      return None
    # set the root to be the current node for the loop
    current_node = self.root
    # loop while there is a right
    while current_node.right:
      current_node = current_node.right

    # return the last node
    return current_node

  def get_min(self):
    '''
      getMin() -> int:\n 
      perform depth first search
      Calculate the minimum value held in the tree
    '''
    pass
