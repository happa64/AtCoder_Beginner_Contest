# https://atcoder.jp/contests/abc163/tasks/abc163_c
# C - management
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = [0] * n
    for i in range(n - 1):
        res[A[i] - 1] += 1

    for i in res:
        print(i)


if __name__ == '__main__':
    resolve()
