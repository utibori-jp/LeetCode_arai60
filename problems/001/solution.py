"""
Problem: 001 - Two Sum
URL: https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            # print(f"=== i = {i} ====")
            for j in range(i+1, len(nums), 1):
                # print(f"i={i}, num[{i}]={nums[i]}, j={j}, num[{j}]={nums[j]}")
                if nums[i] + nums[j] == target: return [i, j]
        
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([3, 3], 6))
