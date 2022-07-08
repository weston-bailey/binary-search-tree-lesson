from BinaryTree import Node, BinaryTree

# test_node = Node(10)
# test_node.left = Node(5)
# test_node.right = Node(15)
# print(test_node, test_node.left, test_node.right)

test_tree = BinaryTree()
test_tree.insert(15)
test_tree.insert(7)
test_tree.insert(3)
test_tree.insert(9)
test_tree.insert(22)
test_tree.insert(28)
test_tree.insert(29)
print('tree root:', test_tree.root) # 15
print('root\'s left:', test_tree.root.left) # 7
print('root\'s left\'s left:', test_tree.root.left.left) # 3

print('root\'s left\'s right:', test_tree.root.left.right) # 9
print('root\'s right:', test_tree.root.right) # 22
print('root\'s right\'s right:', test_tree.root.right.right) # 28

# test_tree.print()
print('searching for 9:', test_tree.search(9))
print('searching for -1:', test_tree.search(-1))
print(test_tree.size())
print(test_tree.get_max())
print(test_tree.height())
print(test_tree.get_min())

