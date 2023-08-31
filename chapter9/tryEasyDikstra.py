# 간단 다익스트라
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split(' ')) # 노드와 간선의 갯수

start = int(input()) # 시작 노드 번호

#빈리스트 , 노드와 간선 정보를 저장할 예정
graph = [[] for i in range(n+1)] # 연결테이블: 간선 연결 정보를 저장

visited = [False] * (n+1) # 방문테이블: 여부 표시

distance = [INF] * (n+1) #거리테이블: 각 노드의 시작노드로부터 현행 최소 거리

#간선정보 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    # a 에서 b 로 가는 비용 c : 각 간선에 대한 정의 
    graph[a].append((b,c))
    
# 방문안한 노드 중 가장 최단거리가 짧은 노드
def get_smallest_node(): # 미선택 최소 노드 구하기
    min_value = INF # 최소 값을 INF로 가정
    index = 0  #index 0으로 가정
    for i in range(1,n+1): #노드값 값을 돌고 돌아 
        if distance[i] < min_value and not visited[i]: #최소보다 작으며 미방문이면
            min_value = distance[i] # 최솟값 갱신하며
            index = i #최소 인덱스도 갱신한다.
    return index # 다 끝나면 인덱스만 반환

def dijkstra(start):
    distance[start] = 0 # 시작 노드의 노드값을 0 으로 지정
    visited[start] = True # 시작 노드 방문처리
    for j in graph[start]: # [[(b,c),(b,c)][()]] 와 같은 구조다
        # 즉 시작 노드에 연결된 간선에 대해 반복하는 것
        
        distance[j[0]] = j[1] 
        # 노드 값 기록: 도착노드번호 = # 간선 비용
        
    for i in range(n-1): # 모든 노드에 관하여 반복 
        
        now = get_smallest_node() # 최소 노드 번호 할당
        visited[now] = True # 해당 최소 노드 방문 처리
        for j in graph[now]: # 해당 최소 노드와 연결된 노드에 반복처리
            #이전 시작(혹은선택)노드에서 연결된 노드에 값을 '확정'했기에
            #일반적으로 연결된 노드가 최소노드일 경우가 많다.
            cost = distance[now] + j[1]
           #값 = #노드 값 기록:현재 노드값 + 간선거리비용
            if cost < distance[j[0]]:# 만약 본래값보다 위 값이 더 작다면
                distance[j[0]] = cost#도착지의 값은 위의값을 취한다. 

dijkstra(start) # dijkstra 시작 

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])    
    

