# https://atcoder.jp/contests/arc034/submissions/14638951
# A - 首席
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for a, b, c, d, e in scores:
        s = a + b + c + d + e * 110 / 900
        res = max(res, s)
    print(res)


if __name__ == '__main__':
    resolve()
