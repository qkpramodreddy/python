stack = []

stack.append(1)
stack.append(2)
stack.append(3)

stack.pop()
stack.pop()
stack.pop()
stack.append(5)

if not stack:
  print("stack is empty")
else:
  print(f"stack is not empty, top is {stack[-1]}")
