
1.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def function(root,p,q):
            if not root: return None
            if root==p or root==q: return root
            left=function(root.left,p,q)
            right=function(root.right,p,q)
            print(left)
            print(right)
            if left and right: return root
            if left: return left
            if right:return right
            
        return function(root,p,q)

2.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words=set(wordDict)
        queue=collections.deque([0])
        visit=set()
        while queue:
            vertex=q.popleft()
            if vertex=len(s): return True
            for i in range(vertex+1,len(s)+1):
                if i in visit: continue
                if s[vertex:i] in words:
                    queue.append(i)
                    visit.add(i)
        return False


3.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        out=[]
        
        for i in nums: out.append(-i)
        heapq.heapify(out)
        while k:
            k-=1
            temp=heapq.heappop(out)*(-1)
        return temp


        

            
        