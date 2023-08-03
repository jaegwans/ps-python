#부품찾기
import sys,math

n = int(sys.stdin.readline().rstrip()) #가게 물품 갯수
reqList = list(map(int,sys.stdin.readline().rstrip().split())) #가게 물품
m = int(sys.stdin.readline().rstrip()) #요청 
resList = list(map(int,sys.stdin.readline().rstrip().split())) #요청 수량 갯수

result = []

reqList.sort()

# 1억번 이상 -> 이진탐색 필요
for target in resList:
    start = 0
    end = n-1
    # middle = end + start//2
    while start<=end:
        print(start,end)
        mid = (end + start) // 2
        if reqList[mid] == target:
            result.append('yes')
            break
        elif reqList[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if(start>end):
        result.append('no')
    
    
    # while(start<middle): # 같아질때까지 start와 end가
    #     middle = math.floor((end + start)/2)
    #     # print(middle,reqList[middle],item)
    #     # print(start,end)
    #     #중위가 item보다 크다면
    #     if(reqList[middle]>item):
    #         end = middle
    #     elif(reqList[middle]==item): #중위가 item 이라면 
    #         result.append('yes')
    #         break # 이 반복문 탈출
    #     else:# 중위가 작다면
    #         start= middle
    # if(start>=end): #미결
    #     result.append('no')
            

for i in result:
    print(i,end=" ")
    