# https://atcoder.jp/contests/agc012/tasks/agc012_a
# A - AtCoder Group Contest
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = sorted(list(map(int, input().split())))

    res = 0
    for i in range(n):
        res += A[-(i + 1) * 2]

    print(res)


if __name__ == '__main__':
    resolve()
