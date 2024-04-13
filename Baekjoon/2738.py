import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        A[i][j] += temp[j]
        print(A[i][j], end=' ')
    print()