#게임 개발

x,y = map(int, input().split()) # 맵 생성
ux, uy, ud = map(int,input().split()) # 좌표와 방향 0 북 1 2 3
mapArr = []
for _ in range(y):
    dmapArrItem = list(map(int,input().split()))
    mapArr.append(dmapArrItem)
    
# 규칙
# 1. 좌측에 안가본 칸 존재하면 좌측으로 회1전 후 한칸 전진
# 2. 안가본 칸 없으면 회전만 하고 다시 1단계
# 3. 사방 모두 가본 칸이면 or 바다 이면 바라보는 방향 유지한 체로 한칸 뒤로
# 3-1. 뒤가 바다면 움직임을 멈춤

# 북동남서
dx = [0,1,0,-1]
dy = [-1,0,1,0]
dd = [0,1,2,3]

log = []

stack = 0

while True:
    
    if mapArr[uy+dy[ud-1]][ux+dx[ud-1]] == 0 and [uy+dy[ud-1],ux+dx[ud-1]] not in log: #육지며 가보지 않은 곳이면
        ud = dd[ud-1] #회전 후 
        #전진
        ux += dx[ud]
        uy += dy[ud]
        log.append[ux,uy]
    else:
         ud = dd[ud-1] #회전
         stack += 1
    
    if stack == 4: ## 갈곳이 없으면
        stack = 0 # 스택 초기화
        
        
        
        
# 
