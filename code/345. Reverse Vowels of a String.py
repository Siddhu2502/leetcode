class Solution:
    def reverseVowels(self,s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            # if both the values are found swap them
            if s_list[i] in vowels and s_list[j] in vowels:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
            # if the left most found and right most not yet found use the point of that index
            elif s_list[i] in vowels:
                j -= 1
            # if the right most found and the left most not yet found then use this pointer to store that index
            elif s_list[j] in vowels:
                i += 1
            # if neither character is a vowel, move both pointers
            else:
                i += 1
                j -= 1
        # convert the list back to a string and return it
        return ''.join(s_list)