"""
Brute force solution
Time complexity O(n^2)
"""


def dailyTempBruteForce(temperatures):
    ans = []
    for i in range(len(temperatures)):
        if len(ans) < i:
            ans.append(0)
        if i == len(temperatures) - 1:
            ans.append(0)
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                ans.append(j - i)
                break
    return ans


"""
Optimal solution O(n)
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                ans[stack[-1][0]] = index - stack[-1][0]
                stack.pop()
            stack.append([index, temp])

        return ans


# Fall 2023 solution
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        # For each element in temperatures
        for i, temp in enumerate(temperatures):
            # While there are elements in stack and the curr temperature is greater than
            # the temperature in the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # pop the latest index from the stack and update res
                prev_index = stack.pop()
                res[prev_index] = i - prev_index

            stack.append(i)

        return res
