# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root):
            if root == None:
                return ["#"]
            left = dfs(root.left)
            right = dfs(root.right)
            return [str(root.val)] + left + right
        result = dfs(root)
        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.words = data.split()
        def buildTree():
            if not self.words:
                return None
            first = self.words[0]
            self.words = self.words[1:]
            if first == "#":
                return None
            root = TreeNode(int(first))
            root.left = buildTree()
            root.right = buildTree()
            return root
        return buildTree()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
