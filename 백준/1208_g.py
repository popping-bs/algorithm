import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline



N, S  =  map(int, input().split())
nums = list(map(int, input().split()))

mid = N // 2
left = nums[:mid]
right = nums[mid:]

def all_sum(arr):
    res = [0]
    for x in arr:
        res += [v + x for v in res]
    return res

A = all_sum(left)
B = all_sum(right)

A.sort()
B.sort()

i = 0
j = len(B) -1
ans = 0

while i < len(A) and j >=0:

    s = A[i] + B[j]

    if s == S:
        a_val = A[i]
        b_val = B[j]
        a_cnt = 0
        b_cnt = 0
        
        while i < len(A) and A[i] == a_val:
            a_cnt +=1
            i += 1

        while j >= 0 and B[j] == b_val:
            b_cnt += 1
            j -=1

        ans += a_cnt * b_cnt
    elif s < S:
        i += 1

    else:
        j -= 1

if S == 0:
    ans -=1

