class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            ls = sorted(s)
            lt = sorted(t)
            print(ls, lt)
            return ls == lt
