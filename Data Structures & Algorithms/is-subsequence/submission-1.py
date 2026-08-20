class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a=iter(t)
        return all(char in a for char in s)

            