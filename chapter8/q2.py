import sys
# 개미 전사

n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().rstrip().split(' ')))
print(n,arr)

feeds = [0] * n # 기록판 (축적량을 기록함)

feeds[0] = arr[0]
feeds[1] = max(arr[1],arr[0]) # 1까지 열어봤을때 1을 선택했을 수도 있고 0을 선택했을 수도 있다 이에 대한 최댓값을 지정한다.

for i in range(2,n):
    feeds[i] = max(feeds[i-1],feeds[i-2]+arr[i])
    
    
print(feeds[n-1]) # 확인판이기때문에 마지막은 항상 최대축적값을 출력





# for i in range(2,n):
#     arr[i] += max(arr[i-1],arr[i-2]+arr[i])
    
        
        
    

# 결론에 대한 최적로를 찾을 경우 - dp
# 경우 1. n-1이 선택됐을 경우 n 미선택
# 경우 2. n-1이 선택 안됐을 경우 n 선택
