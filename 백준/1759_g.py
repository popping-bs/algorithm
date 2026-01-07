import string
import sys
from collections import deque

abc_letters = list(string.ascii_lowercase)

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

L, C = map(int, input().split())
letters = input().split()
letters.sort()

path = []
vowels =  {'a','e','i','o','u'}


def dfs(start_idx, v_cnt, c_cnt):

    if len(path) == L:
        if v_cnt >=1 and c_cnt>=2:        
            print(''.join(path))
        return
    


    for i in range(start_idx, C):
        ch = letters[i]
        path.append(ch)


        if ch in vowels:
            dfs(i+1, v_cnt+1, c_cnt)
        else:
            dfs(i+1, v_cnt, c_cnt+1)

        path.pop()


dfs(0,0,0)