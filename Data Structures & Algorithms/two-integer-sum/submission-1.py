class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            if target - n not in map:
                map[n] = i
            else:
                return [map[target-n], i]