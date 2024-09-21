import sys
# 입력 받기
n = int(sys.stdin.readline())

# 짝수일 때와 홀수일 때의 처리
if n % 2 == 0:
    # N이 짝수일 때는 1과 2를 번갈아 출력
    result = [1, 2] * (n // 2)
else:
    # N이 홀수일 때는 1과 2를 번갈아 하다가 마지막에 1을 추가
    result = [1, 2] * (n // 2) + [3]

# 결과 출력
print(" ".join(map(str, result)))

# n = int(input())
# ans = [1, 2] * (n//2) + ([3] if n%2 else [])
# print(*ans)