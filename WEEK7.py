
#1
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q=collections.deque([root])
        temp=[]
        out=[]
        while q:
            l=len(q)
            for i in range(l):
                node=q.popleft()
                temp.append(node)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            out.append(temp[-1].val)
            temp=[]
        return out
    
    
#2

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        cache = [[-1] * cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(row, col):
            if cache[row][col] != -1:
                return cache[row][col]
            max_length = 1  # 每个单元格至少是1
            for x, y in directions:
                nx, ny = row + x, col + y
                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > matrix[row][col]:
                    max_length = max(max_length, 1 + dfs(nx, ny))
            cache[row][col] = max_length
            return max_length
        
        max_path = 0
        for i in range(rows):
            for j in range(cols):
                if cache[i][j] == -1:
                    max_path = max(max_path, dfs(i, j))
        
        return max_path

#3
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        out=[]
        def inorder(root):
            if not root: return 
            inorder(root.left)
            out.append(root.val)
            inorder(root.right)
        inorder(root)
        
        return  out[k-1]
