import sys
# 입력 받기
n = int(input())  # 막대기의 개수
heights = [int(sys.stdin.readline()) for _ in range(n)]  # 막대기의 높이 리스트

# 오른쪽에서부터 왼쪽으로 보면서 가장 큰 막대기를 추적
max_height = 0
visible_count = 0

# 오른쪽에서부터 확인
for i in range(n-1, -1, -1):
    if heights[i] > max_height:
        visible_count += 1
        max_height = heights[i]

# 결과 출력
print(visible_count)
