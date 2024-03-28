l = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

s = input()
time = 0
for i in s:
    for index, value in enumerate(l):
        if i in value:
            time += index + 3
            break

print(time)