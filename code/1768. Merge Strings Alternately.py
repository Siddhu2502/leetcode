class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        min_len = min(len(word1), len(word2))
        
        # Merge characters alternately up to min_len
        for i in range(min_len):
            new_string += word1[i] + word2[i]
        
        # Append remaining characters from word1 or word2
        if len(word1) > min_len:
            new_string += word1[min_len:]
        elif len(word2) > min_len:
            new_string += word2[min_len:]
        
        return new_string