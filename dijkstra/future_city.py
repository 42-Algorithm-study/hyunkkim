import math

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
	for b in range(1, n + 1):
		if a == b :
			graph[a][b] = 1

for _ in range(m):
	a, b = map(int, input().split())
	graph[a][b] = 1
    graph[b][a] = 1

w, l = map(int, input().split())

for k in range(1, n + 1):
	for a in range(1, n + 1):
		for b in range(1, n + 1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

if graph[1][l] == INF:
    print("-1 : A to love is INF")
elif graph[l][w] == INF:
    print("-1 : love to work is INF")
else:
    print(graph[1][l] + graph[l][w])

print("\nDone.\n")
