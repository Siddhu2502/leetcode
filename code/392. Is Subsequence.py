class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Initialize two pointers to traverse the strings.
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)  # Check if all characters in s were found in t.