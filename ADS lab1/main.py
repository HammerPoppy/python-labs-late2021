from Node import Node

if __name__ == '__main__':
    #

    print('TASK 1 | Create tree')
    print('Creating tree with data of [1, 5, 10, 8]...')

    tree = Node([1, 5, 10, 8])

    print(tree.get_inorder(tree))
    print('TASK 1 | Done\n')

    #

    print('TASK 2 | Add item to tree')
    print('Adding item of 7 to the tree...')

    tree.insert(7)

    print(tree.get_inorder(tree))
    print('TASK 2 | Done\n')

    #

    print('TASK 3 | Delete item from tree')
    print('Deleting item of 8 from the tree...')

    tree.remove(8)

    print(tree.get_inorder(tree))
    print('TASK 3 | Done\n')

    #

    print('TASK 4 | Delete tree')
    print('Deleting tree...')

    tree.disintegrating_directive()

    print(tree.get_inorder(tree))
    print('TASK 4 | Done\n')

    #

    print('TASK 5 | Check if tree is empty')
    print('Checking if tree is empty...')

    if tree.is_empty():
        result = 'empty'
    else:
        result = 'not empty'

    print('Tree is ' + result)
    print('TASK 5 | Done\n')

    #

    print('TASK 6 | Check if tree has item')
    print('Adding to the tree data of [13, 666, 228, 1337]...')

    tree.insert([13, 666, 228, 1337])

    print(tree.get_inorder(tree))

    # --
    print('Checking if tree has 7...')

    if tree.has(7):
        result = 'has'
    else:
        result = 'has not'

    print('Tree ' + result + ' 7')

    # --
    print('Checking if tree has 13...')

    if tree.has(13):
        result = 'has'
    else:
        result = 'has not'

    print('Tree ' + result + ' 13')

    print('TASK 6 | Done\n')

    #

    print('TASK 7 | Copy tree')
    print('Copying the tree...')

    tree2 = tree.get_copy()

    print(tree.get_inorder(tree))
    print(tree.get_inorder(tree2))
    print('TASK 7 | Done\n')

    #

    print('TASK 8 | Access tree items with 3 methods')

    print('Printing tree items with inorder traversal method...')
    print(tree.get_inorder(tree))

    print('Printing tree items with preorder traversal method...')
    print(tree.get_preorder(tree))

    print('Printing tree items with postorder traversal method...')
    print(tree.get_postorder(tree))

    print('TASK 8 | Done\n')

    #

    print('TASK 9 | Print tree')
    print(tree.get_inorder(tree))
    print('TASK 9 | Done\n')

    #
