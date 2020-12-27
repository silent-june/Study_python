import random

N, X = map(int, input().split())
a = []

for n in range(N):
    a.append(random.randrange(0, 100 + 1))
    if a[n] < X:
        print(a[n], end=" ")
