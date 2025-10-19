import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        sums = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]
        heapq.heapify(sums)

        res = []

        while sums and len(res) < k:
            summ, i, j = heapq.heappop(sums)
            res.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):  # Push next element from same row
                heapq.heappush(sums, (nums1[i] + nums2[j + 1], i, j + 1))

        return res
