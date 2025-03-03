import sys

class Solution:
  def intToRoman(self, num: int) -> str:
    int_roman = { 1: "I", 4: "IV", 5: "V", 9: "IX",
                  10: "X", 40: "XL", 50: "L", 90: "XC",
                  100: "C", 400: "CD", 500: "D", 900: "CM",
                  1000: "M"
                }
    keys = sorted(int_roman.keys(), reverse=True)

    ans = ''

    for key in keys:
      #curr = int(num/key)
      curr = (num//key)
      for i in range(curr):
        ans += int_roman[key]
      num = num % key

    return ans
      
      
num = int(sys.argv[1])
p1 = Solution()
roman = p1.intToRoman(num)
print(num, roman)
