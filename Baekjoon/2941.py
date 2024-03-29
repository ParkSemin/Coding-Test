cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()
cnt = 0

for i in cro:
    if i in s:
        s = s.replace(i, ' ', c:=s.count(i))
        cnt += c

print(cnt + len(s.replace(' ', '')))