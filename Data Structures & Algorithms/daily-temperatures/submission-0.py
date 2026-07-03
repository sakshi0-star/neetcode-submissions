class Solution:
    def dailyTemperatures(Self,temperature):
        res = [0]*len(temperature)
        stack =[]

        for i , t in enumerate(temperature):
            while stack and t>stack[-1][0]:
                stackT ,stackInd =stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([t,i])
        return res