from BinaryTree import Node, BinaryTree

# test_node = Node(10)
# test_node.left = Node(15)
# test_node.right = Node(5)
# print(test_node, test_node.left, test_node.right)

test_tree = BinaryTree()
test_tree.insert(15)
test_tree.insert(7)
test_tree.insert(3)
test_tree.insert(9)
test_tree.insert(22)
test_tree.insert(28)
test_tree.insert(25)
test_tree.insert(10)
test_tree.insert(31)
print('tree root:',test_tree.root)
print('root\'s left:', test_tree.root.left)
print('root\'s left\'s left:', test_tree.root.left.left)

print('root\'s left\'s right:', test_tree.root.right)
print('root\'s right:', test_tree.root.left)
print('root\'s right\'s right:', test_tree.root.right.right)

#test_tree.print()
print('searching for 9:', test_tree.search(9))
print('searching for -1:', test_tree.search(-1))
print('max node:', test_tree.get_max())
print('min node:', test_tree.get_min())
print('size:', test_tree.size())

print("height", test_tree.height())
