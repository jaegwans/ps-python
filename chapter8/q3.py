# 바닥 공사
import sys
n = int(sys.stdin.readline().rstrip())
# 2 * n 
# 타일 1*2(가로),2*1(세로),2*2 각각 경우 1,2,3
# 첫칸에 1 혹은 22 혹은 3 이렇게
d = [0] * 1001 #경우의 수에 관한 db테이블

# f(n) = 이전칸이 2나 3이면 유지 ,1이면 +3
d[1] = 1
d[2] = 3
for i in range(3,n+1):
    d[i] = (d[i-1]+d[i-2]*2)%796796
    
print(d[n])
