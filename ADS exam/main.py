from Tree import Tree

if __name__ == '__main__':
    print('Creating tree with data of [45, 35, 12, 0, 34, 57, 100, 2, 14, 25, 78]...')
    tree = Tree([45, 35, 12, 0, 34, 57, 100, 2, 14, 25, 78])
    print(tree.get_inorder(tree))

    print('Removing 34...')
    tree.remove(34)
    print(tree.get_inorder(tree))

    print('Adding 39...')
    tree.insert(39)
    print(tree.get_inorder(tree))

    print('Printing inorder traversal...')
    print(tree.get_inorder(tree))
