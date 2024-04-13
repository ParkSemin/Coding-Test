max = 0
x, y = 0, 0

for i in range(9): # O(81)
    t = list(map(int, input().split()))
    for j in range(9):
        if max < t[j]:
            max = t[j]
            x, y = i, j

print(max)
print(x+1, y+1) 