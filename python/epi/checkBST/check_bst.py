


class BST(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



def check_bst(tree):
    if tree is None:
        return True

    if not ((tree.left is None or tree.left.data <= tree.data) and (tree.right is None or tree.right.data >= tree.data)):
        return False

    is_left_bst = True
    if tree.left is not None:
        is_left_bst = check_bst(tree.left)

    is_right_bst = True
    if tree.right is not None:
        is_right_bst = check_bst(tree.right)

    return is_left_bst and is_right_bst




def main():
    tree = BST(3)
    tree.left = BST(2)
    tree.left.left = BST(1)
    tree.right = BST(5)
    tree.right.left = BST(4)
    tree.right.right = BST(6)


    print check_bst(tree)
    tree.data = 10
    print check_bst(tree)


if __name__ == '__main__':
    main()
