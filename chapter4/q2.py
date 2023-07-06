# #시각
# #3이 포함된 시각 카운팅
# hour = int(input())
# count = 0
# # hour 0~23
# for i in range(hour+1):
#     if(i%10 == 3 or i//10 ==3): # //로 몫만 취함
#         count += 1   ## 이러면 분 초가 해당이 안될때 카운팅이 안되는 예외 발생
        
#     for j in range(60):
#         if(j%10 == 3 or j//10 ==3):
#             count += 1 # 추가적인 카운트 증가 생성 : 분이 3인 경우 카운트 추가가 하나 더 되어버림
  
#         for k in range(60):
#             if(k%10 == 3 or k//10 ==3):
#                 count += 1
               

#시각
#3이 포함된 시각 카운팅
hour = int(input())
count = 0
# hour 0~23
for i in range(hour+1):
        
    for j in range(60):
  
        for k in range(60): 
            result = str(i)+str(j)+str(k)
            if '3' in result:
                count += 1
               
print(count)