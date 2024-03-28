a, b = map(list, input().split())

a[0], a[2] = a[2], a[0]
b[0], b[2] = b[2], b[0]

a = int("".join(a))
b = int("".join(b))

print(a) if a>b else print(b)