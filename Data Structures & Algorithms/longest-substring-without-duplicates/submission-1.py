class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        i = 0
        max_len = 0
        for j in range(len(s)):

            if s[j] not in mp:
                mp[s[j]] = 1
            
            else:
                mp[s[j]] += 1

            

            while mp[s[j]] > 1:
                mp[s[i]] -= 1
                i += 1

            max_len = max(max_len,j-i+1)

        return max_len

        