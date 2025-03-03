from collections import deque

de = deque(['name', 'age', 'DOB'])

print(de)

de.popleft()
print(de)
de.append('name')
print(de)
de.pop()
print(de)
de.appendleft('name')
print(de)
