class Solution:
    def videoStitching(self, clips, time: int) -> int:
        clips.sort()
        end,cnt=0,0
        i=0
        while end<time:
            mend=end
            while i<len(clips) and clips[i][0]<=end:
                mend=max(mend,clips[i][1])
                i+=1
            if mend==end: return -1
            end=mend
            cnt+=1
        return cnt


s=Solution()
s.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10)