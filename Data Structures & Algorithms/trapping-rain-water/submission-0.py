class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water =0
        for i in range(n):
            leftmax = max(height[:i+1])
            rightmax = max(height[i:])
            water += min(leftmax,rightmax) -height[i]
        return water
