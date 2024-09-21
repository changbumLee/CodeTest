def backtrack(N, M, sequence, visited):
    # 길이가 M인 수열을 찾으면 출력
    if len(sequence) == M:
        print(" ".join(map(str, sequence)))
        return
    
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            sequence.append(i)
            backtrack(N, M, sequence, visited)
            sequence.pop()  # 마지막에 추가한 숫자를 다시 제거
            visited[i] = False  # 방문 표시를 해제

# 입력 받기
N, M = map(int, input().split())

# 방문 여부를 기록할 리스트와 빈 수열
visited = [False] * (N + 1)

# 백트래킹 호출
backtrack(N, M, [], visited)