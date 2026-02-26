class Solution:
    def areIsomorphic(self, s1, s2):
        for i in range(len(s1)):
            if s1.index(s1[i]) != s2.index(s2[i]):
                return False
        return True