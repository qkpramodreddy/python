def fun1(x, y):
  if x == 0:
    return y
  else:
    print(f"func1({x}, {y})")
    return x + fun1(x-1, x+y)

a = fun1(10, 5)
print(a)

def fun2(n):
  if n == 1:
    return 0
  else:
    return 1 + fun2(n//2)

a = fun2(10)
print(a)

def fun3(n):
  if n == 0:
    return
  fun3(n//2)
  print(n%2, end="")

fun3(16)
