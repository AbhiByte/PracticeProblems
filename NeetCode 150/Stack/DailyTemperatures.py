'''
Brute force solution
Time complexity O(n^2)
'''
def dailyTempBruteForce(temperatures):
  ans = []
  for i in range(len(temperatures)):
      if len(ans) < i:
          ans.append(0)
      if i == len(temperatures) - 1:
          ans.append(0)
      for j in range(i+1, len(temperatures)):
          if temperatures[j] > temperatures[i]:
              ans.append(j-i)
              break
  return ans

'''
Optimal solution
'''
