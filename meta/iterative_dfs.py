# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



root = TreeNode(2, TreeNode(1), TreeNode(33, TreeNode(25), TreeNode(40)))

# In-order traversal
stack = []
current_node = root
result = []

while stack or current_node:
    if current_node:
        stack.append(current_node)
        current_node = current_node.left
    else:
        current_node = stack.pop()
        result.append(current_node.val)
        current_node = current_node.right

print(result)

# Pre-order traversal
result = []
stack = []
current_node = root
previous_node = None

while stack or current_node:
    if current_node:
        result.append(current_node.val)
        stack.append(current_node)
        current_node = current_node.left
    else:
        previous_node = stack.pop()
        current_node = previous_node.right

print(result)

# Post-order traversal
result = []
stack = []
current_node = root
previous_node = None

while stack or current_node:
    if current_node:
        stack.append(current_node)
        current_node = current_node.left
    else:
        top_node = stack[-1]
        if top_node.right and top_node.right != previous_node:
            current_node = top_node.right
        else:
            result.append(top_node.val)
            previous_node = stack.pop()

print(result)
