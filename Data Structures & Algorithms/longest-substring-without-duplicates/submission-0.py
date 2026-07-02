class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0 
        for i in range(n):
            for j in range(i,n):
                substring = s[i:j+1]
                if len(substring) == len(set(substring)):
                    ans  = max(len(substring),ans)
        return ans
