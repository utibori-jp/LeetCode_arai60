import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.sol = Solution()

    @pytest.mark.parametrize("inputs, expected", [
        # basic cases
        (([1, 2, 2, 1], [2, 2]), [2]),
        (([4, 9, 5], [9, 4, 9, 8, 4]), [9, 4]),
        # edge cases
        (([], [1, 2, 3]), []),
        (([1, 2, 3], []), []),
        (([1], [1]), [1]),
        # no intersection
        (([1, 2, 3], [4, 5, 6]), []),
        # all elements intersect
        (([1, 2, 3], [3, 2, 1]), [1, 2, 3]),
        # duplicates in both arrays
        (([1, 1, 1, 2], [1, 1, 2, 2]), [1, 2]),
    ])
    def test_intersection(self, inputs, expected):
        assert sorted(self.sol.intersection(*inputs)) == sorted(expected)
