"""
Problem: 929 - Unique Email Addresses
URL: https://leetcode.com/problems/unique-email-addresses/description/
"""

from typing import List
import re

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # 初回（2026/05/02）
        pattern_plus = r"\+.*"
        pattern_dots = r"\."
        email_set = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = re.sub(pattern_plus, "", local_name)
            local_name = re.sub(pattern_dots, "", local_name)
            email_set.add(f"{local_name}@{domain_name}")
        return len(email_set)

        # 2回目（）
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numUniqueEmails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
