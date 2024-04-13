'''
<문제 해설>
- 각 색종이의 너비는 100(10*10)
- 색종이는 100개 이하

<입력>
- N : 색종이의 수
- N개의 줄 : 색종이의 시작 좌표(x, y)

<출력>
- 색종이가 붙은 넓이의 합
- 색종이가 겹치는 부분을 잘 계산해야함

<풀이 방향>
ver 1) - 구현 실패
- 색종이의 개수 * 100에서 색종이가 겹치는 부분의 너비를 빼면 될 것 같음
- 색종이가 겹치려면 두 색종이의 x, y좌표를 뺀 값의 절댓값이 10보다 작아야 함

ver 2) - 
- 도화지 크기(100*100)만큼의 2차원 리스트 사용
- 색종이를 도화지에 채울 때마다 해당 범위의 리스트 값을 True로 설정
'''
# ver 2)
# 1. 도화지 리스트 선언 및 색종이 개수 입력 받기
board = [ [False]*100 for _ in range(100) ] # 100*100의 좌표라고 보면 됨. 색종이를 붙이지 않았다면 False, 붙였다면 True
N = int(input())

# 2. 색종이 좌표 입력받음과 동시에 색종이를 붙이면서 해당 범위의 값을 1로 설정
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        board[i][y:y+10] = [1] * 10

# 3. 도화지 내의 색종이가 부착된 영역(1)의 총 개수를 구함
cnt = 0
for i in board:
    cnt += i.count(1)
print(cnt)

# ver 1) 실패
'''
# 1. 입력
N = int(input())
total = N * 100 # 겹치는 부분을 고려하지 않은 전체 너비
paper = sorted([list(map(int, input().split())) for _ in range(N)])

# 2. 겹치는 부분의 너비 뺄셈
for i in range(len(paper) - 1):
    for j in range(i+1, len(paper)):
        if abs(paper[i][0] - paper[j][0]) < 10: 
            if abs(paper[i][1] - paper[j][1]) < 10: # 겹치는 상황
                # (3, 7)과 (5, 2)라면 가로로는 8(10 - (5-3))만큼 겹치고 세로로는 5(10- (7-2))만큼 겹친다
                t = ( 10 - abs(paper[i][0] - paper[j][0]) ) * ( 10 - abs(paper[i][1] - paper[j][1]) )
                print(t)
                total -= t
                break

# 3. 출력
print(total)
'''