n = int(input())
cnt = 0

for _ in range(n):
    s = input()
    b = True
    for i in range(len(s)):
        if s.count(s[i]) > 1:
            if s[i+1] == s[i]:
                s = s.replace(s[i], ' ', 1)
            else:
                b = False
                break
    if b: cnt += 1

print(cnt)