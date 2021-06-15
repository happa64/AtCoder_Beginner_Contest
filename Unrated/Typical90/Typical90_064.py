# https://atcoder.jp/contests/typical90/submissions/23361982
# 064 - Uplift（★3）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))

    diff = [b - a for a, b in zip(A, A[1:])]
    res = sum([abs(a) for a in diff])
    for _ in range(q):
        l, r, v = map(int, input().split())
        l -= 1
        r -= 1
        if 0 <= l - 1 < n - 1:
            res -= abs(diff[l - 1])
            diff[l - 1] += v
            res += abs(diff[l - 1])
        if 0 <= r < n - 1:
            res -= abs(diff[r])
            diff[r] -= v
            res += abs(diff[r])
        print(res)


if __name__ == '__main__':
    solve()
