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
        result = [pair[1] for pair in pairs[-k:]]
        return result