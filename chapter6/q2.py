#성적이 낮은 순
# 입 n , 이름 점수
# 출 이름 (점수 오름차순)

n = int(input())

arr = []
for _ in range(n):
    dName,dScore= input().split()
    arr.append((dName,int(dScore)))
def keyForScore(data):
    return data[1]
    
    
arrSort = sorted(arr,key=keyForScore)# sorted는 기본함수 sort는 리스트의 메서드이다.

for i in arrSort:
    print(i[0],end=" ")
