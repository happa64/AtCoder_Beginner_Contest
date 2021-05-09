# https://codeforces.com/contest/1519/submission/115781585
# D - Maximum Sum of Products


def calc(l, r):
    global max_diff
    diff = 0
    while l >= 0 and r < n:
        diff += A[l] * (B[r] - B[l]) + A[r] * (B[l] - B[r])
        max_diff = max(max_diff, diff)
        l -= 1
        r += 1


n = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
res = sum(a * b for a, b in zip(A, B))
max_diff = 0
for i in range(n):
    calc(i, i)
    calc(i, i + 1)
print(res + max_diff)
