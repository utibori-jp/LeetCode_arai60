"""
Problem: 349 - Intersection of Two Arrays
URL: https://leetcode.com/problems/intersection-of-two-arrays/
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 初回（2026/05/01）
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        ans = []
        for num1 in nums1_set:
            if num1 in nums2_set: ans.append(num1)
        return ans 

        # 2回目（2026/05/02）
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.intersection([1, 2, 2, 1], [2, 2]))
