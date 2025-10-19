from heapq import *

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        mapp = [(capital[i], profits[i]) for i in range(len(profits))]
        heapify(mapp)

        affordables = []

        for _ in range(k):
            # move all affordable projects into the max-heap
            while mapp and mapp[0][0] <= w:
                cap, prof = heappop(mapp)
                heappush(affordables, -prof)  # max-heap via negative profits

            if not affordables:
                break  # no project can be done with current capital

            w += -heappop(affordables)  # pick the most profitable available project

        return w
