import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

sx1, sy1, ex1, ey1 = map(int, input().split())      # 첫번째 박스의 위치 좌표
sx2, sy2, ex2, ey2 = map(int, input().split())      # 두번째 박스의 위치 좌표

# 두 박스가 만나지 않는 경우 True를 반환하는 함수 / 아닐 경우 False 반환
def isNull():
    if sx1 > ex2 or ex1 < sx2 or sy1 > ey2 or ey1 < sy2: return True  
    return False

# 두 박스가 점으로 만나는 경우 True를 반환하는 함수 / 아닐 경우 False 반환
def isPoint(): 
    if ex1 == sx2 or ex2 == sx1:            # x축이 만나는 경우
        return ey1 == sy2 or ey2 == sy1     # y축도 만나는지 확인
    return False

# 두 박스가 선으로 만나는 경우 True를 반환하는 함수 / 아닐 경우 False 반환
def isLine(): 
    # x축 또는 y축이 만나는지 확인
    return ex1 == sx2 or ex2 == sx1 or ey1 == sy2 or ey2 == sy1

if isNull(): print("NULL")
elif isPoint(): print("POINT")
elif isLine(): print("LINE")
else: print("FACE")
