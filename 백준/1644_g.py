import sys


sys.stdin = open("input.txt",'r')
input = sys.stdin.readline

N = int(input())

is_prime = [True] * (N+1)
is_prime[0] = is_prime[1] = False


#어떤 수가 합성수라면, 그 수를 만드는 곱셉에는 반드시
#루트 한 값보다 작거나 같은 숫자가 하나 있음.
for i in range(2, int(N**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, N+1, i):
            is_prime[j] = False

primes = [ i for i in range(2, N+1) if is_prime[i]]

n_primes = len(primes)

sum = 0
left = 0
count = 0
for right in range(n_primes):
    sum+=primes[right]

    while sum > N:
        
        sum -= primes[left]
        left += 1

    if sum == N:
        count+=1

print(count)