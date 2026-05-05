N = int(input())                        # rook의 개수
B = [input().strip() for _ in range(N)] # 체스판 정보
cols = [0] * N              # col 별 rook의 배치 여부

# 재귀함수
# row : rook을 놓을 행 (rook은 행별로 1개씩만 놓을 수 있음) 
def func(row):
    res = 0                                 # 배치 가능한 경우의 수
    
    # 함수 return 조건
    # rook을 N개 놓은 경우
    if row >= N: return 1

    # rook을 더 놓을 수 있는 경우
    for col in range(N):                    # rook을 열 마다 1개씩 놓아 본다
        if B[row][col] == '#': continue     # 놓을 수 있는 곳인지 확인
        if cols[col]: continue              # 이미 해당 열에 놓여진 경우
        cols[col] = 1                       # 해당 열에 rook 배치 표시
        res += func(row + 1)
        cols[col] = 0                       # 해당 열의 rook 배치 표시 해제
    
    return res

print(func(0))
