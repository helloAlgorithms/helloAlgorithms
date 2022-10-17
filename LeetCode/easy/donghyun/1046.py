class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones) > 1:
            x, y = heappop(stones), heappop(stones)
            heappush(stones, -max(0, y - x))
        return -stones[0]