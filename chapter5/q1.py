#음료수 얼려먹기
y,x = map(int,input().split())

print(y,x)

graph = []

for _ in range(y):
    graph.append(list(map(int,input())))
    
print(graph)
visited = [[False]*x for _ in range(y)]

count = 0


# dfs(graph,v,visited)
def dfs(i,j):
    for di in [i-1,i,i+1]:
        for dj in [j-1,j,j+1]:
            if(-1<di<y and -1<dj<x and visited[di][dj] == False and graph[di][dj] == 0): #범위를 만족하고 방문하지 않았으면서 0이면
                visited[di][dj] = True
                dfs(di,dj)
        
    

for i in range(y):
    for j in range(x):
        if visited[i][j] == False and graph[i][j] == 0:
            count += 1
            dfs(i,j)
        
print(visited)
print(count)

# visited와 graph, 재귀를 이용 = dfs