from collections import deque

class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right
        
def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

#problem 1

#Understand:
    #input: descriptions [[str, str, int]]
        #[parent, child, left/right]
    #output: node root
    #constraint:
    # edge case: Description is empty
#Plan:
    #1st pass - create nodes, store in map
    #2nd pass - link children
    
    #nodemap (str : node): 
    #for description in descriptions
        #parent, child, dir = description[0], description[1], description[2]
        #if parent not in nodemap:
            #nodemap[parent] = TreeNode(parent)
        #parent = nodemap[parent]
        #if child not in nodemap:
            #nodemap[child] = TreeNode(child)
        #child = nodemap[child]
        #if dir == 0:
            #parent.left = child
        #else:
            #parent.right = child
    #return nodemap[descriptions[0][0]]
    
"""
description1 = []
descriptions1 = [
    ["Chocolate Chip", "Peanut Butter", 1],
    ["Chocolate Chip", "Oatmeal Raisin", 0],
    []
]
"""

def build_cookie_tree(descriptions):
    if not descriptions:
        return None
    nodemap = {}
    for description in descriptions:
        parent, child, dir = description[0], description[1], description[2]
        if parent not in nodemap:
            nodemap[parent] = TreeNode(parent)
        parent = nodemap[parent]
        if child not in nodemap:
            nodemap[child] = TreeNode(child)
        child = nodemap[child]
        if dir == 0:
            parent.right = child
        else:
            parent.left = child
    return nodemap[descriptions[0][0]]

if __name__ == '__main__':
    descriptions1 = [
        ["Chocolate Chip", "Peanut Butter", 1],
        ["Chocolate Chip", "Oatmeal Raisin", 0],
        ["Peanut Butter", "Sugar", 1]
    ]

    descriptions2 = [
        ["Ginger Snap", "Snickerdoodle", 0],
        ["Ginger Snap", "Shortbread", 1]
    ]

    # Using print_tree() function included at top of page
    print_tree(build_cookie_tree(descriptions1))
    print_tree(build_cookie_tree(descriptions2))