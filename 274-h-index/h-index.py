class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort()
        n = len(citations)
        left, right = 0, n - 1
        h = 0

        while left <= right:
            mid = (left + right) // 2
            # number of papers >= citations[mid] citations
            papers = n - mid # 3
            
            if citations[mid] >= papers:
                h = papers
                right = mid - 1 # shrink for a smaller index
            else:
                left = mid + 1
        
        return h

        # [0,1,5,7,15]



        