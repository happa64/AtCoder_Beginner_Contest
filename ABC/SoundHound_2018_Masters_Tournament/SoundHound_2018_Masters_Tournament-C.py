# https://atcoder.jp/contests/soundhound2018-summer-qual/submissions/14465469
# C - Ordinary Beauty
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, d = map(int, input().split())

    if d == 0:
        res = (m - 1) / n
    else:
        res = (m - 1) * 2 * (n - d) / (n ** 2)
    print(res)


if __name__ == '__main__':
    resolve()
