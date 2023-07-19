import sys
# 위에서 아래로
arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
    


arrs = sorted(arr,reverse=True)

for i in arrs:
    print(i,end=' ') # 줄바꿈을 대신할 end 속성 지정
    # %은 붙을 수 있음 vscode 터미널 문제
    