class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            # check if needed is in seen
            if needed in seen:
                return [seen[needed], i]
            # otherwise store current number and its index
            seen[nums[i]] = i