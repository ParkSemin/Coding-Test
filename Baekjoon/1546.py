n = int(input())
score = list(map(int, input().split()))
m = max(score)

print(sum([i/m*100 for i in score])/n)