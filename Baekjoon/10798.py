paint = [""] * 15 # 단어 별 최대 글자 수는 15자리라 했으므로 길이 15의 문자열 리스트 선언
for _ in range(5):
    for index, value in enumerate(input()):
        paint[index] += value # 입력받은 단어의 0번째는 paint[0]에 추가, 1번째는 [1]에 추가하는 방식

for i in paint:
    if len(i) != 0: # 값이 있는 paint 리스트 요소만 출력
        print(i, end='')