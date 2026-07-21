class Solution:
    def largestRectangleArea(self, heights):
        stack = []          # (start_index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index

            stack.append((start, h))

        n = len(heights)

        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (n - index))

        return maxArea