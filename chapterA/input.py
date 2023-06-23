import sys

n = int(input())
lists = list(map(int, input().split())) # 암기

print(n,lists)

lists = list(map(int, sys.stdin.readline().rstrip().split())) # 암기


print(n,lists)

# 형변환에 문제가 생길수 있다
# + 연산자에 수와 문자열을 함께 사용할시 str(수) 를 해주자

print(f"number is {n}")