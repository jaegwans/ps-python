# 큰 수의 법칙
import sys


n,m,k = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split())) 
# readline() 으로 입력시 공백에 추가되어 rstrip()필수
# n은 배열 갯수
# m은 더할수 있는 횟수
# k는 인덱스 상 연속 가능한 횟수
result = 0
idx = 0
g = k

arr.sort(reverse=True)
print(arr)

if arr[0] != arr[1]:
    for _ in range(m):
        if(g==0): # 연속 횟수가 0이 되었을때
            result += arr[1]
            g = k # 연속 횟수를 초기화한다.
            print(arr[1],"a")
        else:
            result += arr[0] ## 해당 인덱스 값을 추가하고 
            g -= 1 # 연속횟수를 깎는다.
            print(arr[0],"b")
    
        
else: # 같다면
     for _ in range(m):
         result += arr[0] ## 해당 인덱스 값을 추가하고 
         print(arr[0],"c")

print(result)
    
            
    
            

# 반복되는 수열을 이용하여 효율적으로 풀 수있다.