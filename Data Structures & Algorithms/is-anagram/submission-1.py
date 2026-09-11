class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1
        t_freq = {}
        for char in t:
            t_freq[char] = t_freq.get(char,0) + 1
        s_freq = {}
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1
        t_freq = {}
        for char in t:
            t_freq[char] = t_freq.get(char,0) + 1
        if len(s) != len(t):
                return False

        for char in s_freq:
                if s_freq[char] != t_freq.get(char, 0):
                        return False

        return True
