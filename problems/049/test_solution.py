import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.sol = Solution()

    @pytest.mark.parametrize("strs, expected", [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["abc", "bca", "cab", "xyz", "zyx"], [["abc", "bca", "cab"], ["xyz", "zyx"]]),
        (["ab", "ba", "cd", "dc", "ef"], [["ab", "ba"], ["cd", "dc"], ["ef"]]),
    ])
    def test_groupAnagrams(self, strs, expected):
        actual = self.sol.groupAnagrams(strs)
        assert sorted([sorted(g) for g in actual]) == sorted([sorted(g) for g in expected])
