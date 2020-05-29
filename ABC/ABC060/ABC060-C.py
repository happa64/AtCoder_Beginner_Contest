# https://atcoder.jp/contests/arc073/tasks/arc073_a
# C - Sentou
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, t = map(int, input().split())
    T = list(map(int, input().split()))

    res = 0
    for i in range(1, n):
        if T[i - 1] + t < T[i]:
            res += t
        else:
            res += T[i] - T[i - 1]

    print(res + t)


if __name__ == '__main__':
    resolve()
