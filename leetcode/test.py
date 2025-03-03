import sys
a = "12345678"

n = len(a)
print(n)
for i in range(n):
  for j in range(i, n):
    print(i, j)

for i in range(0,1):
  print("pramod", i)

print(a[0:0])

index = int(sys.argv[1])
print(a)
print("----")
print(n)
print(a[index])
