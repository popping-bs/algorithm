import sys
from collections import deque


sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

t = int(input())

def sieve(n=10000):
    is_prime = [True] * n
    is_prime[0] = [False]
    is_prime[1] = [False]
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            step = i
            start = i* i
            for j in range(start, n , step):
                is_prime[j] = False

    return is_prime

is_prime = sieve()

def bfs(a,b):
    dist = [-1]*10000
    q = deque([a])
    dist[a] = 0

    while q:
        cur = q.popleft()
        if cur == b:
            return dist[cur]
        
        s = list(str(cur))
        for pos in range(4):
            original = s[pos]
            for d in "0123456789":
                if d == original:
                    continue
                if pos == 0 and d == "0":
                    continue

                s[pos] = d 
                nxt = int("".join(s))

                if is_prime[nxt] and dist[nxt] == -1:
                    dist[nxt] = dist[cur] +1
                    q.append(nxt)


            s[pos] = original

    return -1

for _ in range(t):
    a, b = map(int,input().split())
    ans = bfs(a,b)
    print( ans if ans != -1 else "Impossible")






def bfs2(a,b):
    dist = [-1] * 10000
    dist[a] = 0
    q = deque([a])

    while q:
        cur = q.popleft()
        if cur == b:
            return dist[cur]
        
        s = list(str(cur))
        for pos in range(4):
            original_digit = s[pos]
            for d in "012456789":
                if pos == 0 and d == "0":
                    continue

                if d == original_digit:
                    continue
                s[pos] = d
                nxt = int("".join(s))

                if is_prime[nxt] and dist[nxt] == -1:
                    dist[nxt] = dist[cur] +1
                    q.append(nxt)

            s[pos] = original_digit

    return -1


            