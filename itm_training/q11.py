class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
#O(1) set takes for membership
        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False