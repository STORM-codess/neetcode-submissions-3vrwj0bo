class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}
        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]]+=1

            else:
                seen[s[i]]=1

        for i in range(len(t)):
            if t[i] in seen:
                seen[t[i]]-=1

        for value in seen.values():
            if value != 0:
                return False
        return True
                

            

        