a = [1, 1, 2, 2, 2, 8]
b = list(map(int, input().split()))

for i, j in zip(a, b):
    print(i-j, end=' ')