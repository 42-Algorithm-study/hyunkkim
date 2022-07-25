import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
# 이게 노드 정보.
graph = [[] for i in range (n + 1)]
# 최단거리 정보 테이블.
distance = [INF] * (n + 1)

# 간선 정보를 입력받음.
# underbar가 뭘 의미하는지 모르겠음.
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드는 0으로 시작하고, 
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 큐가 있으면, 
    while q:
        # 최단 거리 노드를 뽑아서, 
        dist, now = heapq.heappop(q)
        # ( 이미 처리된 경우라면 무시하고)
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 노드들을 반복문으로 확인을 하는데, 
        for i in graph[now]:
            cost = dist + i[1]
            # 거리가 더 짧다면 업데이트를 해줌.
            # cost update?
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력.
for i in range(1, n + 1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
