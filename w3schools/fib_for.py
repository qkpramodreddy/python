import sys

def fibo(n):
  prev2 = 0
  prev1 = 1
  print(prev2, end=" ")
  print(prev1, end=" ")
  for i in range(n):
    print(prev2 + prev1, end=" ")
    temp = prev2 + prev1
    prev2 = prev1
    prev1 = temp
fibo(int(sys.argv[1]))
