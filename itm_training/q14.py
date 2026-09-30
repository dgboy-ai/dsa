class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for value in nums:
            result ^= value
        return result