"""
Problem: 001 - Two Sum
URL: https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 初回（単純解法）
        # for i in range(len(nums)-1):
        #     # print(f"=== i = {i} ====")
        #     for j in range(i+1, len(nums), 1):
        #         # print(f"i={i}, num[{i}]={nums[i]}, j={j}, num[{j}]={nums[j]}")
        #         if nums[i] + nums[j] == target: return [i, j]
        
        # pass

        # 2回目（2026/04/29）
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index: return [num_to_index[complement], i]
            num_to_index[num] = i

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([3, 3], 6))
