class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        i = 0
        for i in range(len(nums)):
            value = nums[i]
            if value in seen:
                return True
            else:
                seen.add(value)
        return False
#TIME: O(n)
#SPACE: O (n) -> n pode armazenar n elementos no PIOR caso