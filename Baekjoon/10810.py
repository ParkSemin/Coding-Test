import sys

n, m = map(int, input().split())
basket = [0] * n

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for c in range(i-1, j):
        basket[c] = k

for i in basket:
    print(i, end=' ')