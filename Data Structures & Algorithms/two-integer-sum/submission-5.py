class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for j, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], j]
            seen[num] = j
obj=Solution()
a=obj.twoSum([-1,-2,-3,-4,-5],-8)