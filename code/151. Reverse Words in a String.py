class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into individual words
        words = s.split()
        
        # Reverse the order of words
        reversed_words = list(reversed(words))
        
        # Join the reversed words back into a string
        outstring = ' '.join(reversed_words)
        
        return outstring