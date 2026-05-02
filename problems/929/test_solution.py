import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.sol = Solution()

    @pytest.mark.parametrize("inputs, expected", [
        # basic
        ((["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"],), 2),
        ((["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"],), 3),
        # edge: single email
        ((["single@example.com"],), 1),
        # edge: all map to the same address
        ((["a.b+c@x.com", "ab+d@x.com", "a.b@x.com"],), 1),
        # special: plus without local suffix, dots only
        ((["test+@x.com", "test@x.com"],), 1),
        ((["t.e.s.t@x.com", "test@x.com"],), 1),
    ])
    def test_numUniqueEmails(self, inputs, expected):
        assert self.sol.numUniqueEmails(*inputs) == expected
