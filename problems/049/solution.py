"""
Problem: 049 - Group Anagrams
URL: https://leetcode.com/problems/group-anagrams/description/
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
    # 初回回答（2026/04/29）
        # anagram_map = defaultdict(list)

        # for word in strs:
        #     key = "".join(sorted(word))
        #     anagram_map[key].append(word)
        
        # return list(anagram_map.values())

    # 2回目（2026/04/30）
        anagram_map = defaultdict(list)
        for word in strs:
            char_freq = [0] * 26
            for ch in word:
                char_freq[ord(ch) - ord('a')] += 1
            anagram_map[tuple(char_freq)].append(word)
        return list(anagram_map.values())


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
