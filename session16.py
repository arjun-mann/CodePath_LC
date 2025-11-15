from collections import deque
import itertools


#print_tree:
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
    
#build_tree:
def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
    
    


# #problem 1

# #Understand:
#     #input: node
#         #given root of binary tree (design)
#         #traverse in trie order (level by level, left to right)
#     #output: [[str]]
#     #constraint: empty
# #Plan:

# class Puff():
#      def __init__(self, flavor, left=None, right=None):
#         self.val = flavor
#         self.left = left
#         self.right = right

# def listify_design(design):
#     if not design: return []
#     queue = deque()
#     queue.append([design, 1]) #[[1,1]]
#     depth = 1
#     levels = []
#     level = []
#     while queue:
#         currnode, currdepth = queue.popleft() #[1,1] | [2,2] | [3,2]
#         if currdepth > depth:
#             depth = currdepth #2
#             levels.append(level) #[[1]]
#             level = []
#         level.append(currnode.val) #[1] | [2] | [3]
#         if currnode.left: #True (2) | False | False
#             queue.append([currnode.left, depth+1]) #[2, 2]
#         if currnode.right: #False | False
#             queue.append([currnode.right, depth+1])  #[3, 2]
#     levels.append(level)
#     return levels
    
# #Problem 2

# #Understand:
#     #input: node cupcakes
#     #output: list[str]
#     #constraint:
# #Plan:

# #None

# #  1
# # 2 3
# #4

# def zigzag_icing_order(cupcakes):
#     if not cupcakes: return []
#     queue = deque() #
#     queue.append([cupcakes, 1])  #[1,1]
#     depth = 1
#     levels = []
#     level = []
#     flag = True
#     while queue: #[1,1] | [4,3]
#         currnode, currdepth = queue.popleft() #[1,1] | [2,2] | [3,2]
#         if currdepth > depth: #2 > 1 | 2 > 2 | 3 > 2
#             depth = currdepth #2
#             if flag: #True | False
#                 levels.append(level) #levels = [[1]]
#             else:
#                 levels.append(level[::-1]) #levels = [[1], [3,2]]
#             flag = not flag #flag = False | flag = True
#             level = [] #level = []
#         level.append(currnode.val) #[1] | [2] | [2, 3] | [4]
#         if currnode.left: #True | True | False | False
#             queue.append([currnode.left, depth+1]) #q = [2,2] | q = [3,2], [4,3]
#         if currnode.right: #True | False | False | False
#             queue.append([currnode.right, depth+1]) #q = [3,2]
#     if flag: #True
#         levels.append(level) #levels = [[1], [3,2], [4]]
#     else:
#         levels.append(level[::-1])
#     merged_list = list(itertools.chain.from_iterable(levels))
#     return merged_list

# if __name__ == '__main__':
#     #None
    
#     # 1 
#     #2 3
    
#     # croquembouche = Puff("Vanilla", 
#     #                 Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
#     #                 Puff("Strawberry"))
#     # print(listify_design(croquembouche))
    
#     flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
#     cupcakes = build_tree(flavors)
#     print(zigzag_icing_order(cupcakes))
    
#Problem 3
#Understand:
    #input:
    #output:
    #constraint:
#Plan:
    
class TreeNode():
     def __init__(self, order_size, left=None, right=None):
        self.val = order_size
        self.left = left
        self.right = right

def larger_order_tree(orders):
    

    def dfs(node, cumilative_sum):
        if not node:
            return cumilative_sum

        cumilative_sum = dfs(node.right, cumilative_sum)

        cumilative_sum += node.val
        node.val = cumilative_sum

        cumilative_sum = dfs(node.left, cumilative_sum)

        return cumilative_sum

    dfs(orders, 0)
    return orders


# using build_tree() function included at top of page
order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
orders = build_tree(order_sizes)

# using print_tree() function included at top of page
print_tree(larger_order_tree(orders))
  
#Problem 4:
#Understand:
    #input: node order_tree node, order
        #given root of binarytree order_tree and TreeNode object order
        #return next order to fulfill that day
        #nearest node in same level
    #output: 
    #constraint:
        #regular BFS
        #once you find target
            #if next neighbor is layer down return None
            #if next neighbor is same layer, return 

