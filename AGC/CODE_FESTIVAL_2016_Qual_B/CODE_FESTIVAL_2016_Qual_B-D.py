# https://atcoder.jp/contests/code-festival-2016-qualb/submissions/18667654
# D - Greedy customers
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    res = A[0] - 1
    mi = 2
    for i in range(1, n):
        if mi < A[i]:
            res += (A[i] - 1) // mi
        else:
            mi = max(mi, A[i] + 1)
    print(res)


if __name__ == '__main__':
    resolve()
