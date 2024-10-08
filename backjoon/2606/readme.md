### 문제 해결 방법:
이 문제는 그래프 탐색 문제로, 컴퓨터 간의 연결을 그래프로 보고 DFS 또는 BFS를 사용하여 바이러스가 퍼질 수 있는 컴퓨터들을 탐색하면 됩니다.

### 해결 절차:
그래프의 각 노드는 컴퓨터를 나타내며, 간선은 두 컴퓨터 간의 연결을 나타냅니다.
1번 컴퓨터에서 시작하여 DFS 또는 BFS를 통해 연결된 모든 컴퓨터를 탐색합니다.
1번 컴퓨터를 제외하고 바이러스에 감염된 컴퓨터의 수를 구합니다.

### 설명:
그래프 생성:
각 컴퓨터의 연결 정보를 인접 리스트로 표현합니다. 컴퓨터 𝑢와 𝑣가 연결되어 있으면, graph[u]에 𝑣를 추가하고 graph[v]에 𝑢를 추가합니다.

### DFS 탐색:
DFS로 1번 컴퓨터에서 시작하여 연결된 모든 컴퓨터를 탐색합니다. 탐색된 컴퓨터는 visited 배열에서 True로 표시됩니다.

### 결과 출력:
visited 배열에서 True로 표시된 노드(컴퓨터) 수를 셉니다. 1번 컴퓨터는 제외해야 하므로, visited.count(True) - 1이 감염된 컴퓨터 수가 됩니다.

