# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        print(dummy)
        quick,slow=dummy,dummy
        while quick.next and quick.next.next:
            slow=slow.next
            quick=quick.next.next
        return slow.next
        


        







class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        start = end = head
        # find the k-th node (the end node for the current group)
        for _ in range(k):
            if not end: return head # not enough items (< k) => remain the order
            end = end.next
        # reverse the current group with k nodes
        newHead = self.reverse(start, end)
        # after reverse start is the end for the group, link it with the next reversed group
        start.next = self.reverseKGroup(end, k)

        return newHead

    # reverse diapason [start:end), end not inclusive
    def reverse(self, start, end):
        prev = None
        while start != end:
            start.next, start, prev = prev, start.next, start
        return prev # return head node of the reversed group
    
    
    
    
    
    
    
    
    
    
    
    
    
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N=9
        rows=[set() for _ in range(N)]
        cols=[set() for _ in range(N)]
        boxes=[set() for _ in range(N)]
        print(rows)
        for r in range(N):
            for c in range(N):
                val=board[r][c]
                if val==".":
                    continue
                if val in rows[r]:
                    return False
                rows[r].add(val)
                if val in cols[c]:
                    return False
                cols[c].add(val)
                index=(r//3)  +(c//3)*3
                if val in boxes[index]:
                
                    return False
                boxes[index].add(val)
        return True
            
            
        