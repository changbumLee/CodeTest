def dfs(graph, visited, node):
    visited[node] = True  # 현재 노드를 방문 처리
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

# 입력 받기
n = int(input())  # 컴퓨터 수
m = int(input())  # 네트워크 상에서 연결된 컴퓨터 쌍의 수

# 그래프 초기화 (1부터 n까지 사용하므로 n+1 크기로 생성)
graph = [[] for _ in range(n + 1)]

# 네트워크 정보 입력받기
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 처리 리스트
visited = [False] * (n + 1)

# 1번 컴퓨터부터 DFS 탐색 시작
dfs(graph, visited, 1)

# 1번 컴퓨터를 제외한 감염된 컴퓨터 수 출력
# visited에서 1번 컴퓨터는 제외하고 True인 노드 개수를 센다.
print(visited.count(True) - 1)







# BFS로 해결하는 방법:
# from collections import deque

# def bfs(graph, visited, start):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         node = queue.popleft()
#         for neighbor in graph[node]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 queue.append(neighbor)

# # 입력 받기
# n = int(input())  # 컴퓨터 수
# m = int(input())  # 네트워크 상에서 연결된 컴퓨터 쌍의 수

# # 그래프 초기화
# graph = [[] for _ in range(n + 1)]

# # 네트워크 정보 입력받기
# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# # 방문 처리 리스트
# visited = [False] * (n + 1)

# # BFS 탐색
# bfs(graph, visited, 1)

# # 감염된 컴퓨터 수 출력
# print(visited.count(True) - 1)
# 설명:
# BFS 탐색은 DFS와 유사하게, 1번 컴퓨터에서 시작하여 연결된 모든 컴퓨터를 탐색합니다. BFS는 큐를 사용해 레벨 순서대로 탐색합니다.
# 시간 복잡도:
# 시간 복잡도는 
# 𝑂
# (
# 𝑁
# +
# 𝑀
# )
# O(N+M)로, 
# 𝑁
# N은 컴퓨터의 수, 
# 𝑀
# M은 연결된 컴퓨터 쌍의 수입니다. 
# 𝑁
# ,
# 𝑀
# N,M이 최대 100이므로 충분히 효율적으로 해결할 수 있습니다.
