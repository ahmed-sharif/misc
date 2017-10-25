class Tree(object):
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

a = Tree(1)
b = Tree(2)
c = Tree(3)
d = Tree(4)
e = Tree(5)
f = Tree(6)
g = Tree(7)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g


def preorder(root):
    if root:
        print root.data
        preorder(root.left)
        preorder(root.right)


def clone_tree(root, new_root):
    if root:
        # print root.data
        new_root.data = root.data
        if root.left:
            new_root.left = Tree()
            clone_tree(root.left, new_root.left)
        if root.right:
            new_root.right = Tree()
            clone(root.right, new_root.right)

preorder(a)

a = Tree(3)
b = Tree(5)
c = Tree(1)
d = Tree(4)
e = Tree(2)
f = Tree(6)


a.left = b
a.right = e

e.left = f

b.left = c
b.right = d

print

newtr = Tree()
preorder(a)




