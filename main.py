from BinaryTree import BinaryTree

def main():
  # Some Test Code
  test_tree = BinaryTree()
  test_tree.insert(5)
  test_tree.insert(2)
  test_tree.insert(1)
  test_tree.insert(3)
  test_tree.insert(10)
  test_tree.insert(7)
  test_tree.insert(6)
  test_tree.insert(9)
  test_tree.insert(8)
  test_tree.insert(-5)
  test_tree.insert(4)
  test_tree.print()
  print('Search for for 5 should return 5:', test_tree.bfs(5))
  print('Search for 11 should return False:', test_tree.bfs(11))
  print('Height should be 5:', test_tree.height())
  print('Size should be 10:', test_tree.size())
  print('Max Val should be 10:', test_tree.get_max())
  print('Min Val should be -5:', test_tree.get_min())
  # print(test_tree.level_order())
  # print(test_tree.inorder_traversal())

if __name__ == "__main__":
  main()