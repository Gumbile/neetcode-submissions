class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0] * len(temperatures)

        for i in range(len(temperatures)-1,-1,-1):
            currTemp = temperatures[i]
            
            while stack and currTemp >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                sol[i] = stack[-1] - i

            stack.append(i)

        return sol
