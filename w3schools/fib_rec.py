import sys
prev2 = 0
prev1 = 1

print(prev2)
print(prev1)
count = 2


def fibonacci(prev1, prev2):
  global count
  if count <= 19:
    new_fibo = prev1 + prev2
    print(new_fibo)
    prev2 = prev1
    prev1 = new_fibo
    count += 1
    fibonacci(prev1, prev2)
  else:
    return

fibonacci(prev1, prev2)

