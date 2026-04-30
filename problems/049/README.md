# 049 - Group Anagrams

- URL: https://leetcode.com/problems/group-anagrams/description/

## Problem Statement

`Medium` `Topics` `Companies`

Given an array of strings `strs`, group the **anagrams** together. You can return the answer in **any order**.

### Example 1:
**Input:** strs = ["eat","tea","tan","ate","nat","bat"]  
**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]  
**Explanation:**
* There is no string in strs that can be rearranged to form `"bat"`.
* The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
* The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

### Example 2:
**Input:** strs = [""]  
**Output:** [[""]]

### Example 3:
**Input:** strs = ["a"]  
**Output:** [["a"]]

### Constraints:
* $1 \le \text{strs.length} \le 10^4$
* $0 \le \text{strs}[i].\text{length} \le 100$
* `strs[i]` consists of lowercase English letters.
