class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for char in nums:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        pairs = []
        for i in count:
            pairs.append([count[i], i])
        pairs.sort()
        result = [pairs[i][1] for i in range(len(pairs) - 1, len(pairs) - k - 1, -1)]
        return result