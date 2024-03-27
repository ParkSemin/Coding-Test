num = sorted([int(input()) for _ in range(28)])

for i in range(1, 30+1):
    if i not in num:
        print(i)