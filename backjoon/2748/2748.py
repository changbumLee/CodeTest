import sys
# 피보나치 수를 계산하는 함수
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # 피보나치 수를 저장할 배열
    fib = [0] * (n + 1)
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# 입력 받기
n = int(sys.stdin.readline())

# n번째 피보나치 수 출력
print(fibonacci(n))