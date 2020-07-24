# https://atcoder.jp/contests/code-festival-2018-quala/submissions/15395799
# B - みかん
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, a, b = map(int, input().split())
    A = [0] * n
    for _ in range(m):
        l, r = map(int, input().split())
        for i in range(l - 1, r):
            A[i] = 1
    cnt = sum(A)
    res = a * cnt + b * (n - cnt)
    print(res)


if __name__ == '__main__':
    resolve()
