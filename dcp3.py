
#Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.
#DCP3
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# serialize a tree into a string
def serialize(root):

    # use an in-order traversal!
    # initialize an empty string
    # recursively call on left, root, right

    if root is None:
        return ''
    else:
        serStr = serialize(root.left) + "()"
        serStr += root.val + "()"
        serStr += serialize(root.right) + "()"
    return serStr

import re
def deserialize(s):

    s = re.split("\(\)+", s)
    print (s)

def dcp3test():

    node = node = Node('root', Node('left', Node('left.left')), Node('right'))

    mystr = serialize(node)
    print(mystr)
    deserialize(mystr)
    #assert deserialize(serialize(node)).left.left.val == 'left.left'
dcp3test()