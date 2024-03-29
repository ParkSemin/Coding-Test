s = []
d = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

for _ in range(20):
    temp = input().split()[1:]
    if temp[1] == 'P':
        continue

    s.append(temp)

sum1 = 0
sum2 = 0
for c, rank in s:
    sum1 += float(c) * d[rank]
    sum2 += float(c)

print(sum1/sum2)