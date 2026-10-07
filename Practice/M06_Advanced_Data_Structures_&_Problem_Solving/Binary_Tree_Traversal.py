
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# Tree structure        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# Tree Traversal techniques
'''
1. DFS
   1. pre-order(Root - Left - Right)
   2. in-order(Left - Root - Right)
   3. post-order(Left - Right - Root)
2. BFS
   1. level-order(Level - 0, Level - 1, Level - 2, ...)
   '''

def pre_order(root):
    if not root:
        return 
    print(root.data,end=" -> ")
    pre_order(root.left)
    pre_order(root.right)

print("pre_order")
pre_order(root)  


def In_order(root):
    if root:
        In_order(root.left) 
        print(root.data,end = " -> ")
        In_order(root.right)
print("In_order Traversal")        
In_order(root)        


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data,end = " -> ")
print("post_order Traversal")
post_order(root)

from collections import deque
def Level_order(root):
    if root is None:
        return
    d = deque([root]) 
    while d:
        node = d.popleft() 
        print(node.data,end= "-> ")  
        if node.left:
            d.append(node.left) 
        if node.right:
            d.append(node.right)
print("level order")
Level_order(root)            