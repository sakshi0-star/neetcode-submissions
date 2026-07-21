from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        need = Counter(t)          # Frequency of characters in t
        window = {}                # Frequency of current window

        have = 0
        needCount = len(need)

        left = 0
        minLen = float('inf')
        start = 0

        for right in range(len(s)):

            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # Character frequency satisfied
            if ch in need and window[ch] == need[ch]:
                have += 1

            # Try shrinking the window
            while have == needCount:

                if (right - left + 1) < minLen:
                    minLen = right - left + 1
                    start = left

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        if minLen == float('inf'):
            return ""

        return s[start:start + minLen]