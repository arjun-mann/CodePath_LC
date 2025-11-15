#problem 1: Grafting Apples
#Understand:
    #input: value, left, right
        #you are grafting different varieties of apple
        #given TreeNode, create binary tree
            #text representing each node should be used as value
            
    #output:
    #constraint:
#Plan:

from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
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
        
    def calculate_yield(root):
        x1 = root.left.val
        x2 = root.right.val
        op = root.val
        if op == "+":
            return x1 + x2
        elif op == "-":
            return x1 - x2
        elif op == "*":
            return x1 * x2
        else:
            return x1 / x2
        
        
if __name__ == "__main__":
    root = TreeNode("Trunk")
    root.left = TreeNode("Mcintosh")
    root.right = TreeNode("Granny Smith")
    root.left.left = TreeNode("Fuji")
    root.left.right = TreeNode("Opal")
    root.right.left = TreeNode("Crab")
    root.right.right = TreeNode("Gala")
    # root.print_tree()
    
    apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
    print(apple_tree.calculate_yield())
    
#problem 2: Calculating Yield
#Understand: 
    #input: root node
        #
    #output: int
    #constraint: 
#Plan: 

    
