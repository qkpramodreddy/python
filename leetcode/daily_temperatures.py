class Solution:

  def dailyTemperatures(self, temperatures: list) -> list:
    stack = []
    length = len(temperatures)
    answer = [0] * length
    for i in range(length):
      while stack and temperatures[stack[-1]] < temperatures[i]:
        print(temperatures[-1])
        j = stack.pop()
        answer[j] = i - j
      stack.append(i)
    print(answer)
    return answer

obj = Solution()

temperatures = [73,74,75,71,69,72,76,73]

ans = obj.dailyTemperatures(temperatures)

print(ans)
