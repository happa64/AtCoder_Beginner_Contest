# https://atcoder.jp/contests/abc061/submissions/12318355
# B - Counting Roads
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    res = [0] * n
    for i in range(m):
        a, b = map(int, input().split())
        res[a - 1] += 1
        res[b - 1] += 1

    for i in res:
        print(i)


if __name__ == '__main__':
    resolve()

