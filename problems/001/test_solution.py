import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.sol = Solution()

    @pytest.mark.parametrize("inputs, expected", [
        # 基本ケース
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
        # エッジケース: 要素数が最小 (2要素)
        (([1, 2], 3), [0, 1]),
        # 特殊ケース: 負数を含む
        (([-3, 4, 3, 90], 0), [0, 2]),
        # 特殊ケース: target が負数
        (([-1, -2, -3, -4], -3), [0, 1]),
    ])
    def test_twoSum(self, inputs, expected):
        result = self.sol.twoSum(*inputs)
        assert sorted(result) == sorted(expected)
