# https://atcoder.jp/contests/past202104-open/submissions/22052112
# D - K項足し算
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    now = sum(A[i] for i in range(k))
    print(now)
    for i in range(k, n):
        now += -A[i - k] + A[i]
        print(now)


if __name__ == '__main__':
    solve()
