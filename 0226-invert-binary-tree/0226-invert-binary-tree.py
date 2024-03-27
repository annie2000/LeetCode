# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        
        if not root: return None
        q = collections.deque()
        q.append(root)
        
        while q:
            node_num = len(q)
            print("Node_num", node_num)
            print(q)
            for i in range(node_num):
                node = q.popleft()
                
                node.left, node.right = node.right, node.left
                
                if node.left:
                    q.append(node.left)
                    print("node.left", q)
                if node.right:
                    q.append(node.right)
                    print("node.right", q)
        return root
                    
                
            
        
        
        
# DFS
#         if not root: return None
        
#         temp = root.left
#         root.left = root.right
#         root.right = temp
        
        
#         self.invertTree(root.left)
#         self.invertTree(root.right)
        
#         return root


        
        
        