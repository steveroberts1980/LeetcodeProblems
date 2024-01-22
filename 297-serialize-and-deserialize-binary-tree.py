# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    # Serialize using a preorder traversal
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodeVals = []

        def serial(node: TreeNode, nodeVals: []):
            if not node:
                nodeVals.append("Null")
                return

            nodeVals.append(str(node.val))

            serial(node.left, nodeVals)
            serial(node.right, nodeVals)

        serial(root, nodeVals)

        return ",".join(nodeVals)
        
    # Deserialzie using a preorder traversal
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodeVals = str(data).split(",")
        nodeVals.reverse()
        def deserial(nodeVals: list[str]):
            node_value = nodeVals.pop()
            if node_value == "Null":
                return
            
            node = TreeNode(int(node_value))

            node.left = deserial(nodeVals)
            node.right = deserial(nodeVals)

            return node
        
        return deserial(nodeVals)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
        
s = Codec()
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

serial = s.serialize(root)
deserial = s.deserialize(serial)

root = None

serial = s.serialize(root)
deserial = s.deserialize(serial)
