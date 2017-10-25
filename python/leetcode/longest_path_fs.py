


class Node(object):
    def __init__(self, name, children=None):
        self.name = name
        self.children = children
        if not children:
            self.children = []


s1 = Node('file2.ext')

s2 = Node('subsubdir2')
s2.children.append(s1)

s3 = Node('subdir2')
s3.children.append(s2)

s4 = Node('subsubdir1')
s5 = Node('file1.ext')
        
s6 = Node('subdir1')
s6.children.append(s5)
s6.children.append(s4)
        
s7 = Node('dir1')
s7.children.append(s3)
s7.children.append(s6)



def print_node(n, tab=0):
    print '  ' * tab, n.name
    for c in n.children:
        print_node(c, tab + 1)


print_node(s7)



def find_max_path(node):
    mx = 0
    mx_path = ''

    for c in node.children:
        length, path = find_max_path(c)

        if length > mx:
            mx = length
            mx_path = path

    if mx == 0:
        return len(node.name), node.name
    else:
        return len(node.name) + mx, node.name + ',' + mx_path

            
    
print find_max_path(s7)

